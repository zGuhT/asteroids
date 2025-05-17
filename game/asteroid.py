import random
from game.circleshape import CircleShape
from game.constants import *
from game.explosion import ExplosionParticle
from game.functions import wrap_position

class Asteroid(CircleShape):
    """Represents an asteroid in the game, with splitting and rendering logic."""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        # Give it a random direction and speed
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * 1.2

    def draw(self, screen):
        # Draw asteroid with a soft inner fill and bright edge
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (200, 200, 255, 60), (self.radius, self.radius), self.radius)
        pygame.draw.circle(surface, (255, 255, 255, 150), (self.radius, self.radius), self.radius, 2)

        # Wrap effect: draw copies around edges for seamless wrap
        for dx in (-SCREEN_WIDTH, 0, SCREEN_WIDTH):
            for dy in (-SCREEN_HEIGHT, 0, SCREEN_HEIGHT):
                screen.blit(
                    surface,
                    (self.position.x - self.radius + dx, self.position.y - self.radius + dy)
                )

    def update(self, dt):
        # Move asteroid, apply screen wrapping
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)

    def split(self, explosion_group, upgrade_group):
        """
        Split asteroid into smaller asteroids and maybe spawn an upgrade.
        Returns: points for splitting.
        """
        scale = self.radius / ASTEROID_MAX_RADIUS

        # Colorful explosion particles
        color = random.choice([
            (173, 216, 230),  # Light blue
            (255, 182, 193),  # Pink
            (204, 153, 255),  # Purple
            (255, 255, 153),  # Yellow
            (102, 255, 255),  # Aqua
        ])
        for _ in range(int(10 * scale) + 5):
            explosion_group.add(ExplosionParticle(self.position, scale, color))
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            print(f"Splitting asteroid with radius: {self.radius}")
            print("Destroyed small asteroid. +10 points.")
            # 30% chance to spawn an upgrade
            if random.random() < 0.3:
                from game.upgradebubble import UpgradeBubble
                upgrade_type = random.choice(["speed", "shield", "rapid_fire"])
                upgrade_group.add(UpgradeBubble(self.position, upgrade_type))
            return 10  # Points for destroying small asteroid

        # Split into 2 smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle_offset = random.uniform(20, 50)
        directions = [self.rotation + angle_offset, self.rotation - angle_offset]
        for angle in directions:
            new_velocity = pygame.Vector2(0, 1).rotate(angle) * self.velocity.length()
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity
            # Add to appropriate groups if needed by caller

        return 0  # No points for splitting large asteroid