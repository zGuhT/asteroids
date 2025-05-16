# shot.py
from circleshape import *
from constants import SHOT_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, SHOT_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt