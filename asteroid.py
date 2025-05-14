from circleshape import *
from constants import ASTEROID_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_asteroid1_angle = pygame.Vector2(0, 1).rotate(self.rotation + new_angle)
        new_asteroid2_angle = pygame.Vector2(0, 1).rotate(self.rotation - new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for new_asteroid_angle in [new_asteroid1_angle, new_asteroid2_angle]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_asteroid_angle * self.velocity.length()        