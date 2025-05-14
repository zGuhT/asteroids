from circleshape import *
from constants import ASTEROID_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)