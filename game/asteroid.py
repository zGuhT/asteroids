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
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, explosion_group):
        scale = self.radius / ASTEROID_MAX_RADIUS
        if self.radius >= ASTEROID_MAX_RADIUS * 0.9:
            color = (255, 100, 0)
        elif self.radius > ASTEROID_MIN_RADIUS * 1.5:
            color = (255, 200, 50)
        else:
            color = (255, 255, 255)
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