import pygame
import random

class ExplosionParticle(pygame.sprite.Sprite):
    """A single particle for an asteroid explosion."""

    def __init__(self, position, scale=1.0, color=(255, 255, 255)):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.radius = random.randint(2, 5) * scale
        # Random velocity direction and speed
        self.velocity = pygame.Vector2(
            random.uniform(-1, 1), random.uniform(-1, 1)
        ).normalize() * random.uniform(100, 200) * scale
        self.lifetime = 0.4 + 0.2 * scale
        self.color = color

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), int(self.radius))