# asteroid.py
from game.circleshape import *
from game.constants import ASTEROID_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from game.explosion import ExplosionParticle
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * 1.2

    def draw(self, screen):
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        pygame.draw.circle(surface, (255, 255, 255, 180), (self.radius, self.radius), self.radius + 1, 2)

        # Inner translucent fill
        pygame.draw.circle(surface, (200, 200, 255, 60), (self.radius, self.radius), self.radius)

        # Brighter outer ring
        pygame.draw.circle(surface, (135, 206, 250, 200), (self.radius, self.radius), self.radius, 2)

        screen.blit(surface, (self.position.x - self.radius, self.position.y - self.radius))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, explosion_group):
        scale = self.radius / ASTEROID_MAX_RADIUS
        # if self.radius >= ASTEROID_MAX_RADIUS * 0.9:
        #     color = (173, 216, 230)
        # elif self.radius > ASTEROID_MIN_RADIUS * 1.5:
        #     color = (102, 255, 255)
        # else:
        #     color = (255, 255, 255)
        color = random.choice([
            (173, 216, 230),  # Light blue
            (255, 182, 193),  # Pink
            (204, 153, 255),  # Purple
            (255, 255, 153),  # Yellow
            (102, 255, 255),  # Aqua
        ])
        for _ in range(int(10 * scale) + 5):
            explosion_group.add(ExplosionParticle(self.position, scale, color))
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print(f"Splitting asteroid with radius: {self.radius}")
            print("Destroyed small asteroid. +10 points.")
            return 10
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle_offset = random.uniform(20, 50)
        directions = [self.rotation + angle_offset, self.rotation - angle_offset]
        for angle in directions:
            new_velocity = pygame.Vector2(0, 1).rotate(angle) * self.velocity.length()
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity
        return 0