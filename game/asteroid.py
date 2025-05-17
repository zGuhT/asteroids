# asteroid.py
from game.circleshape import *
from game.constants import *
from game.explosion import *
from game.functions import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * 1.2

    def draw(self, screen):
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        # Inner translucent fill
        pygame.draw.circle(surface, (200, 200, 255, 60), (self.radius, self.radius), self.radius)

        # Bright outer edge
        pygame.draw.circle(surface, (255, 255, 255, 150), (self.radius, self.radius), self.radius, 2)

        # True wrap: draw 9 copies
        for dx in (-SCREEN_WIDTH, 0, SCREEN_WIDTH):
            for dy in (-SCREEN_HEIGHT, 0, SCREEN_HEIGHT):
                screen.blit(
                    surface,
                    (self.position.x - self.radius + dx, self.position.y - self.radius + dy)
                )

    def update(self, dt):
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)

    def split(self, explosion_group, upgrade_group):
        scale = self.radius / ASTEROID_MAX_RADIUS

        # Random color for explosion
        color = random.choice([
            (173, 216, 230),  # Light blue
            (255, 182, 193),  # Pink
            (204, 153, 255),  # Purple
            (255, 255, 153),  # Yellow
            (102, 255, 255),  # Aqua
        ])

        # Add explosion particles
        for _ in range(int(10 * scale) + 5):
            explosion_group.add(ExplosionParticle(self.position, scale, color))

        self.kill()

        # Check for smallest bubble
        if self.radius <= ASTEROID_MIN_RADIUS:
            print(f"Splitting asteroid with radius: {self.radius}")
            print("Destroyed small asteroid. +10 points.")

            # 30% chance to spawn an upgrade bubble
            if random.random() < 0.3:
                from game.upgradebubble import UpgradeBubble
                upgrade_type = random.choice(["speed", "shield", "rapid_fire"])
                upgrade_bubble = UpgradeBubble(self.position, upgrade_type)
                upgrade_group.add(upgrade_bubble)

            return 10

        # Spawn 2 smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle_offset = random.uniform(20, 50)
        directions = [self.rotation + angle_offset, self.rotation - angle_offset]

        for angle in directions:
            new_velocity = pygame.Vector2(0, 1).rotate(angle) * self.velocity.length()
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity

        return 0