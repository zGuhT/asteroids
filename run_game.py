# run_game.py
import pygame
from game.main import main

if __name__ == "__main__":
    while True:
        result = main()
        if result == "quit":
            break