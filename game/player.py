# player.py
from game.circleshape import *
from game.constants import *
from game.shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.visible = True
        self.flash_timer = 0
        self.flash_duration = 3  # total flash time in seconds
        self.flash_interval = 0.1  # toggle every 0.1 seconds
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = 400  # units per second²
        self.max_speed = 300     # limit max velocity
        self.friction = 0.98     # velocity decay
        self.image = pygame.image.load("assets/player_thomas.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))  # or adjust as needed
        self.image = pygame.transform.rotate(self.image, 90)  # rotate clockwise 90°

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if not self.visible:
            return  # skip drawing when flashing

        rotated = pygame.transform.rotate(self.image, -self.rotation)
        rect = rotated.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(rotated, rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Handle flashing logic
        if self.flash_timer > 0:
            self.flash_timer -= dt
            if int(self.flash_timer / self.flash_interval) % 2 == 0:
                self.visible = False
            else:
                self.visible = True
        else:
            self.visible = True  # ensure it's visible when not flashing

        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # Acceleration
        if keys[pygame.K_w]:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += direction * self.acceleration * dt
        if keys[pygame.K_s]:
            direction = pygame.Vector2(0, -1).rotate(self.rotation)
            self.velocity += direction * self.acceleration * dt

        # Apply friction
        self.velocity *= self.friction

        # Clamp to max speed
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Update position
        self.position += self.velocity * dt

        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
        self.timer = PLAYER_SHOOT_COOLDOWN