import pygame
import sys
import time
import math

from game.constants import *
from game.player import Player
from game.asteroid import Asteroid
from game.asteroidfield import AsteroidField
from game.shot import Shot
from game.functions import (
    load_high_score,
    save_high_score,
    draw_multiline_text,
    show_title_screen,
    wrap_position,
)

def main():
    """Main game loop and logic."""
    pygame.init()

    # Music & sound
    pygame.mixer.init()
    pygame.mixer.music.load("assets/background_music_thomas.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    shoot_sound = pygame.mixer.Sound("assets/snd_shoot.wav")
    pop_sound = pygame.mixer.Sound("assets/snd_pop.wav")
    boost_sound = pygame.mixer.Sound("assets/snd_boost.wav")
    bomb_sound = pygame.mixer.Sound("assets/snd_bomb.wav")
    for snd in (shoot_sound, pop_sound, boost_sound, bomb_sound):
        snd.set_volume(0.3)

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    upgrade_group = pygame.sprite.Group()

    # Assign groups to sprite classes for auto-registration
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Score and timer variables
    high_score = load_high_score()
    asteroid_score = 0
    timer_score = 0
    total_score = 0
    time_elapsed = 0

    # Player lives and state
    player_lives = 3
    player_immunity = False
    player_immunity_timer = 0
    player_bombs = 3

    # UI
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids: Thomas Edition")
    clock = pygame.time.Clock()
    dt = 0
    upgrade_message = ""
    upgrade_message_timer = 0.0

    # Assets
    heart_image = pygame.image.load("assets/heart.png").convert_alpha()
    heart_image = pygame.transform.scale(heart_image, (48, 48))
    background = pygame.image.load("assets/game_background_thomas.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shoot_sound=shoot_sound)
    asteroidfield = AsteroidField()

    show_title_screen(screen, font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    return "quit"
                if event.key == pygame.K_b and player_bombs > 0:
                    # Bomb: destroy all asteroids on screen
                    for asteroid in list(asteroids):
                        asteroid.split(explosions, upgrade_group)
                    player_bombs -= 1
                    bomb_sound.play()

        # Draw background
        screen.blit(background, (0, 0))

        # Update sprites
        updatable.update(dt)
        explosions.update(dt)
        upgrade_group.update(dt)

        # Asteroid collision handling
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                if player.shield:
                    player.shield = False
                    player.shield_timer = 0
                    print("Shield absorbed the hit!")
                    pop_sound.play()
                    score_from_split = asteroid.split(explosions, upgrade_group)
                    asteroid_score += score_from_split
                    continue  # Skip to next asteroid
                elif not player_immunity:
                    player.kill()
                    player_lives -= 1
                    if player_lives == 0:
                        # Game Over screen
                        if total_score > high_score:
                            high_score = total_score
                            save_high_score(high_score)
                            draw_multiline_text(
                                screen,
                                f"New High Score!!!!!\nTimer Score: {timer_score}\nAsteroid Score: {asteroid_score}\nTotal Score: {total_score}\nPress R to Restart\nEsc to Quit",
                                font, (255, 255, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                            )
                        else:
                            draw_multiline_text(
                                screen,
                                f"Game Over!\nTimer Score: {timer_score}\nAsteroid Score: {asteroid_score}\nTotal Score: {total_score}\nPress R to Restart\nEsc to Quit",
                                font, (255, 255, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                            )
                        pygame.display.flip()

                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return "quit"
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_r:
                                        return "restart"
                                    if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                                        return "quit"
                    else:
                        # Respawn with immunity
                        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        player_immunity = True
                        player_immunity_timer = 3
                        player.flash_timer = 3

            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    pop_sound.play()
                    score_from_split = asteroid.split(explosions, upgrade_group)
                    asteroid_score += score_from_split
                    break

        # Upgrade pickup logic
        for upgrade in upgrade_group:
            if player.get_rect().colliderect(upgrade.get_rect()):
                boost_sound.play()
                if upgrade.type == "speed":
                    player.max_speed = PLAYER_SPEED + 200
                    player.speed_boost_timer += 5.0
                elif upgrade.type == "shield":
                    player.shield_timer += 5.0
                elif upgrade.type == "rapid_fire":
                    player.shoot_cooldown = PLAYER_SHOOT_COOLDOWN * 0.5
                    player.rapid_fire_timer += 5.0
                upgrade.kill()
                upgrade_message = f"{upgrade.type.replace('_', ' ').title()} Activated!"
                upgrade_message_timer = 2.0

        # Display upgrade pickup message
        if upgrade_message_timer > 0:
            upgrade_message_timer -= dt
            msg_surface = font.render(upgrade_message, True, (255, 255, 255))
            msg_rect = msg_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
            screen.blit(msg_surface, msg_rect)

        # Draw all drawable elements
        for obj in drawable:
            obj.draw(screen)
        for particle in explosions:
            particle.draw(screen)
        for upgrade in upgrade_group:
            upgrade.draw(screen)

        # Timing
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

        # Score
        total_score = timer_score + asteroid_score

        # --- BOOST UI: Draw bottom-left ---
        boost_lines = []
        if player.speed_boost_timer > 0:
            boost_lines.append(("Speed Boost", player.speed_boost_timer, (173,255,47)))
        if player.rapid_fire_timer > 0:
            boost_lines.append(("Rapid Fire", player.rapid_fire_timer, (255,105,180)))
        if player.shield_timer > 0:
            boost_lines.append(("Shield", player.shield_timer, (135,206,250)))

        # Draw each boost
        ui_x = 20
        ui_y_start = SCREEN_HEIGHT - 10
        line_height = font.get_linesize() + 4

        for i, (label, timer, color) in enumerate(reversed(boost_lines)):
            txt = font.render(f"{label}: {timer:.1f}s", True, color)
            txt_rect = txt.get_rect(bottomleft=(ui_x, ui_y_start - i * line_height))
            screen.blit(txt, txt_rect)

        # Score display
        score_text = font.render(f"Score: {total_score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        high_score_text = font.render(
            f"High Score: {max(total_score, high_score)}", True, (255, 255, 255)
        )
        high_score_rect = high_score_text.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        screen.blit(high_score_text, high_score_rect)

        # Lives as hearts
        for i in range(player_lives):
            x = SCREEN_WIDTH // 2 - (player_lives * 14) + i * 28
            screen.blit(heart_image, (x, 20))

        # Bomb display
        bomb_text = font.render(f"Bombs: {player_bombs}", True, (255, 200, 0))
        bomb_rect = bomb_text.get_rect(topright=(SCREEN_WIDTH - 20, 70))
        screen.blit(bomb_text, bomb_rect)

        pygame.display.flip()

if __name__ == "__main__":
    while True:
        result = main()
        if result == "quit":
            break