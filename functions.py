# functions.py
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
def load_high_score(filename="highscore.txt"):
    try:
        with open(filename, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0  # Default if file is missing or invalid

# Save high score to text file    
def save_high_score(score, filename="highscore.txt"):
    with open(filename, "w") as file:
        file.write(str(score))