import math
import time
import pygame

from game.circleshape import CircleShape
from game.constants import *
from game.shot import Shot
from game.functions import wrap_position

class Player(CircleShape):
    """Player-controlled spaceship."""

    def __init__(self, x, y, shoot_sound=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.visible = True
        self.flash_timer = 0
        self.flash_duration = 3
        self.flash_interval = 0.1
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = 400
        self.max_speed = 300
        self.friction = 0.98
        self.image = pygame.image.load("assets/player_thomas.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image = pygame.transform.rotate(self.image, 90)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.speed_boost_timer = 0
        self.rapid_fire_timer = 0
        self.shield_timer = 0
        self.shield = False
        self.shoot_sound = shoot_sound

    def draw(self, screen):
        if not self.visible:
            return

        rotated = pygame.transform.rotate(self.image, -self.rotation)
        rect = rotated.get_rect(center=(int(self.position.x), int(self.position.y)))

        # Overlay color for powerups (shield/speed/rapid fire)
        draw_overlay = False
        overlay_color = None
        if self.shield_timer > 0:
            overlay_color = (135, 206, 250, self._overlay_alpha())
            draw_overlay = True
        elif self.speed_boost_timer > 0:
            overlay_color = (173, 255, 47, self._overlay_alpha())
            draw_overlay = True
        elif self.rapid_fire_timer > 0:
            overlay_color = (255, 105, 180, self._overlay_alpha())
            draw_overlay = True

        screen.blit(rotated, rect)
        if draw_overlay:
            overlay = pygame.Surface(rect.size, pygame.SRCALPHA)
            overlay.fill(overlay_color)
            screen.blit(overlay, rect)

    def _overlay_alpha(self):
        # Pulsing alpha for overlays
        alpha = int(80 + 40 * math.sin(time.time() * 10))
        return max(0, min(120, alpha))

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Flashing logic for post-respawn immunity
        if self.flash_timer > 0:
            self.flash_timer -= dt
            self.visible = (int(self.flash_timer / self.flash_interval) % 2 == 1)
        else:
            self.visible = True

        self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += direction * self.acceleration * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction = pygame.Vector2(0, -1).rotate(self.rotation)
            self.velocity += direction * self.acceleration * dt

        self.velocity *= self.friction
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)

        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = self.shoot_cooldown

        # Powerup effects
        if self.speed_boost_timer > 0:
            self.speed_boost_timer -= dt
            if self.speed_boost_timer <= 0:
                self.max_speed = PLAYER_SPEED
        if self.rapid_fire_timer > 0:
            self.rapid_fire_timer -= dt
            if self.rapid_fire_timer <= 0:
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        if self.shield_timer > 0:
            self.shield_timer -= dt
            self.shield = True
            if self.shield_timer <= 0:
                self.shield = False

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
        if self.shoot_sound:
            self.shoot_sound.play()
        self.timer = self.shoot_cooldown

    def check_collisions(self, other):
        # Player collision uses sprite rectangle (not just radius)
        rect = self.image.get_rect(center=self.position)
        dist_x = abs(other.position.x - rect.centerx)
        dist_y = abs(other.position.y - rect.centery)
        if dist_x > (rect.width / 2 + other.radius):
            return False
        if dist_y > (rect.height / 2 + other.radius):
            return False
        return True

    def get_rect(self):
        return self.image.get_rect(center=(int(self.position.x), int(self.position.y)))