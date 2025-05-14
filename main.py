# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *

# import everything from the module
# player.py into the current file
from player import *

# import everything from the module
# asteroid.py into the current file
from asteroid import *

# import everything from the module
# asteroidfield.py into the current file
from asteroidfield import *

# import everything from the module
# shot.py into the current file
from shot import *

import sys

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()