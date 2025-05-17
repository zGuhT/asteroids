import pygame
from game.circleshape import CircleShape
from game.constants import *
from game.functions import wrap_position

class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.image = pygame.image.load("assets/bullet_coal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))

    def draw(self, screen):
        rect = self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        for dx in (-SCREEN_WIDTH, 0, SCREEN_WIDTH):
            for dy in (-SCREEN_HEIGHT, 0, SCREEN_HEIGHT):
                screen.blit(self.image, rect.move(dx, dy))

    def update(self, dt):
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)