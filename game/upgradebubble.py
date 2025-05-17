import pygame
import random
from game.constants import *

class UpgradeBubble(pygame.sprite.Sprite):
    """A powerup bubble that floats around the screen."""

    def __init__(self, position, upgrade_type):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.radius = 12
        self.type = upgrade_type
        self.velocity = pygame.Vector2(
            random.uniform(-1, 1), random.uniform(-1, 1)
        ).normalize() * random.uniform(30, 60)

    def update(self, dt):
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def draw(self, screen):
        color_map = {
            "speed": (173, 255, 47),
            "shield": (135, 206, 250),
            "rapid_fire": (255, 105, 180)
        }
        color = color_map.get(self.type, (255, 255, 255))
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def get_rect(self):
        return pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)