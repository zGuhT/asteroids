import pygame
import random
from game.asteroid import Asteroid
from game.constants import *

class AsteroidField(pygame.sprite.Sprite):
    """
    Handles automatic spawning of asteroids at the screen edges.
    Spawns asteroids at a regular interval, with random sizes and velocities,
    and always from a random screen edge.
    """

    # Definitions for edges:
    # Each entry is: (direction_vector, position_function)
    # position_function: maps a float 0-1 to a coordinate on the edge
    edges = [
        [pygame.Vector2(1, 0),  lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],                    # Left edge
        [pygame.Vector2(-1, 0), lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],      # Right edge
        [pygame.Vector2(0, 1),  lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)],                     # Top edge
        [pygame.Vector2(0, -1), lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)],      # Bottom edge
    ]

    def __init__(self):
        # Use the containers set by the main game for group membership
        super().__init__(self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Instantiates and adds an Asteroid at the specified position with given radius and velocity.
        Asteroid is automatically added to groups due to containers mechanism.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        # No need to add to groups, handled by containers

    def update(self, dt):
        """
        Update spawn timer, and spawn a new asteroid when the timer exceeds the spawn rate.
        Asteroids spawn at a random edge, with random velocity and size.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            # Choose a random edge and position
            edge = random.choice(self.edges)
            direction = edge[0]
            # Random speed between 40 and 100
            speed = random.randint(40, 100)
            # Randomize the direction slightly (spread ±30°)
            velocity = direction * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            # Edge position: random coordinate along the chosen edge
            position = edge[1](random.uniform(0, 1))
            # Random asteroid size (kind)
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)