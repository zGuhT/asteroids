import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Abstract base class for all round game objects.
    Inherits from pygame.sprite.Sprite for use with groups.
    """

    def __init__(self, x, y, radius):
        # Sprite group assignment if using containers
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass  # To be overridden

    def update(self, dt):
        pass  # To be overridden

    def check_collisions(self, other):
        # Returns True if this circle collides with another circle
        return self.position.distance_to(other.position) < self.radius + other.radius