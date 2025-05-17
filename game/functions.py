# functions.py
import pygame
from game.constants import *

# Function used to draw multiple lines to the screen
def draw_multiline_text(screen, text, font, color, center_pos, line_spacing=10):
    lines = text.split("\n")
    rendered_lines = [font.render(line, True, color) for line in lines]

    # Calculate total height
    total_height = sum(line.get_height() for line in rendered_lines) + (len(rendered_lines) - 1) * line_spacing

    # Top position to start drawing from
    start_y = center_pos[1] - total_height // 2

    for line_surface in rendered_lines:
        rect = line_surface.get_rect(center=(center_pos[0], start_y + line_surface.get_height() // 2))
        screen.blit(line_surface, rect)
        start_y += line_surface.get_height() + line_spacing

# Load high score from text file
def load_high_score(filename="data/highscore.txt"):
    try:
        with open(filename, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0  # Default if file is missing or invalid

# Save high score to text file    
def save_high_score(score, filename="data/highscore.txt"):
    with open(filename, "w") as file:
        file.write(str(score))

def wrap_position(pos, screen_width, screen_height):
    x, y = pos
    return pygame.Vector2(
        x % screen_width,
        y % screen_height
    )

def show_title_screen(screen, font):
    # Load and scale the background
    bg = pygame.image.load("assets/title_background_thomas.png").convert()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Render title and instructions
    title_text = font.render("ThomAsteroids", True, (30, 30, 255))
    start_text = font.render("Press [SPACE] to Start", True, (255, 255, 255))
    quit_text = font.render("Press [Q] or [ESC] to Quit", True, (255, 255, 255))

    # Main title screen loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Start game
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
        screen.blit(bg, (0, 0))
        # Center title near top, and instructions near center/bottom
        screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH//2, 120)))
        screen.blit(start_text, start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)))
        screen.blit(quit_text, quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 90)))
        pygame.display.flip()