import pygame
from game.main import main

# Main game runner loop
if __name__ == "__main__":
    while True:
        result = main()
        if result == "quit":
            break