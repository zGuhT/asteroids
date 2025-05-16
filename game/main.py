# main.py
import pygame
import sys

from game.constants import *
from game.player import Player
from game.asteroid import Asteroid
from game.asteroidfield import AsteroidField
from game.shot import Shot
from game.functions import load_high_score, save_high_score, draw_multiline_text

def main():
    pygame.init()

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups to sprite classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Score tracking
    high_score = load_high_score()
    asteroid_score = 0
    timer_score = 0
    total_score = 0
    time_elapsed = 0

    # Other variables
    player_lives = 3
    player_immunity = False
    player_immunity_timer = 0

    # Font and display
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    # Game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

        # Clear screen
        screen.fill((0, 0, 0))

        # Update all updatable objects
        updatable.update(dt)

        # Collision detection
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                if player_immunity == False:
                    player.kill()
                    player_lives -= 1
                    if player_lives == 0:
                        print("Game over!")
                        if total_score > high_score:
                            high_score = total_score
                            save_high_score(high_score)
                            draw_multiline_text(
                                screen,
                                f"New High Score!!!!!\nTimer Score: {timer_score}\nAsteroid Score: {asteroid_score}\nTotal Score: {total_score}\nPress R to Restart\nEsc to Quit",
                                font,
                                (255, 255, 255),
                                (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                            )
                        else:
                            draw_multiline_text(
                                screen,
                                f"Well Fuck.. It's Game Over!\nTimer Score: {timer_score}\nAsteroid Score: {asteroid_score}\nTotal Score: {total_score}\nPress R to Restart\nEsc to Quit",
                                font,
                                (255, 255, 255),
                                (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                            )
                        pygame.display.flip()

                        # Only enter this loop if the player is truly out of lives
                        if player_lives == 0:
                            pygame.display.flip()

                            # Pause and wait for input
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return "quit"
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_r:
                                            return "restart"
                                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                                            return "quit"
                    else:
                        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        player_immunity = True
                        player_immunity_timer = 3
                        player.flash_timer = 3

            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    score_from_split = asteroid.split()
                    asteroid_score += score_from_split
                    break  # Avoid multiple hits on same asteroid

        # Draw everything
        for obj in drawable:
            obj.draw(screen)

        # Timer-based score (1 point per second)
        dt = clock.tick(60) / 1000
        time_elapsed += dt
        if time_elapsed >= 1.0:
            seconds = int(time_elapsed)
            timer_score += seconds
            time_elapsed -= seconds
        if player_immunity:
            player_immunity_timer -= dt
            if player_immunity_timer <= 0:
                player_immunity = False

        # Combine scores
        total_score = timer_score + asteroid_score

        # Render score
        score_text = font.render(f"Score: {total_score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Render high score
        if total_score > high_score:
            high_score_text = font.render(f"High Score: {total_score}", True, (255, 255, 255))
        else:
            high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        high_score_rect = high_score_text.get_rect(topright=(SCREEN_WIDTH - 20, 20))  # 20px padding from top-right corner
        screen.blit(high_score_text, high_score_rect)

        # Render remaining lives
        if player_lives == 3:
            remaining_lives_text = font.render(f"Remaining Lives ({player_lives}):  <3  <3  <3", True, (255, 255, 255))
        elif player_lives == 2:
            remaining_lives_text = font.render(f"Remaining Lives ({player_lives}):  <3  <3", True, (255, 255, 255))
        else:
            remaining_lives_text = font.render(f"Remaining Lives ({player_lives}):  <3", True, (255, 255, 255))
        remaining_lives_rect = remaining_lives_text.get_rect(midtop=(SCREEN_WIDTH / 2, 20))  # 20px padding from top-centre
        screen.blit(remaining_lives_text, remaining_lives_rect)

        # Update display
        pygame.display.flip()

if __name__ == "__main__":
    while True:
        result = main()
        if result == "quit":
            break