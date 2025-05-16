# asteroid.py
from circleshape import *
from constants import ASTEROID_WIDTH, ASTEROID_MIN_RADIUS
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

    def split(self):
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