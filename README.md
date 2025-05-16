# Asteroids (Python / Pygame)

A classic-style arcade **Asteroids** game clone built using **Pygame**. This version features player movement, asteroid splitting, shooting mechanics, scoring, lives, respawning with invincibility, and persistent high score tracking.

---

## Features

- Player-controlled ship with rotation and thrust
- Bullet shooting and cooldown timer
- Asteroid field generation with edge spawning
- Asteroid splitting into smaller fragments
- Scoring system:
  - +1 point per second survived
  - +10 points per small asteroid destroyed
- High score saving to `data/highscore.txt`
- Life system with 3 lives and on-death respawning
- 3-second invincibility (with visual flashing) after respawn
- Game over screen with restart and quit options

---

## Controls

| Key         | Action                  |
|-------------|--------------------------|
| W           | Move forward             |
| S           | Move backward            |
| A / D       | Rotate left/right        |
| SPACE       | Shoot                    |
| R           | Restart (after game over)|
| Q or ESC    | Quit                     |

---

## Requirements

- Python 3.10+
- Pygame 2.0+

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## File Structure

```
astroids/
├── assets/                    # (optional) images, sounds, etc.
├── data/
│   └── highscore.txt          # Persistent high score data
├── game/
│   ├── __init__.py
│   ├── main.py
│   ├── player.py
│   ├── asteroid.py
│   ├── asteroidfield.py
│   ├── shot.py
│   ├── circleshape.py
│   ├── constants.py
│   └── functions.py
├── .gitignore
├── README.md
├── requirements.txt
└── run_game.py                # Main game entry point
```

---

## High Score System
- High scores are saved to `data/highscore.txt`.
- Automatically updated if you beat the previous record.

---

## Customization Tips
- Want more difficulty? Decrease `ASTEROID_SPAWN_RATE` in `constants.py`
- Want faster action? Adjust `PLAYER_SPEED` or `PLAYER_SHOOT_COOLDOWN`
- Add powerups or effects by extending the `Shot` or `Player` classes

---

## How to Run

```bash
python run_game.py
```

Make sure your virtual environment is activated and dependencies are installed.

---

## License
This project is open for educational and non-commercial use. Modify it, expand it, and learn from it!