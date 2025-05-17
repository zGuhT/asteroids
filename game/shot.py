# shot.py
from game.circleshape import *
from game.constants import SHOT_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.image = pygame.image.load("assets/bullet_coal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))  # Adjust size if needed


    def draw(self, screen):
        rect = self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(self.image, rect)

    def update(self, dt):
        self.position += self.velocity * dt