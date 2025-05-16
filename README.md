# Asteroids (Python / Pygame)
<!-- Built as part of a personal assignment to refresh and rebuild foundational coding skills -->

A classic-style arcade **Asteroids** game clone built using **Pygame**. This game was originally built as part of a self-guided assignment to help refresh my coding knowledge and re-engage with Python development. It features player movement, asteroid splitting, shooting mechanics, scoring, lives, respawning with invincibility, and persistent high score tracking.

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

## Planned Features (Assignment Suggestions)
- ~~Add a scoring system~~
- ~~Implement multiple lives and respawning~~
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

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

## Change Log

### v1.212001 (2025-05-16)
- G: v1.212001 updated readme AGAIN again (i swear this is the last)

### v1.212 (2025-05-16)
- G: v1.212 updated readme AGAIN again

### v1.211 (2025-05-16)
- G: v1.211 updated readme AGAIN

### v1.21 (2025-05-16)
- G: v1.21 updated readme

### v1.2 (2025-05-16)
- Added `update_changelog.py` script for automated changelog generation and Git integration

### v1.11 (2025-05-16)
- Restructured project folders for clarity and scalability
- Added `README.md` and `.gitignore`

### v1.1 (2025-05-16)
- Implemented scoring system based on survival time and asteroid destruction
- Added player lives and respawn mechanics with temporary invincibility

### v1.0 (2025-05-15)
- Complete playable version of Asteroids

### v0.9 (2025-05-14)
- Added shooting and projectile system

### v0.8 (2025-05-14)
- Player object created with rotation and movement

### v0.1 (2025-05-14)
- Initial playable prototype with movement and basic asteroid logic

---

## Customization Tips
- Want more difficulty? Decrease `ASTEROID_SPAWN_RATE` in `constants.py`
- Want faster action? Adjust `PLAYER_SPEED` or `PLAYER_SHOOT_COOLDOWN`

---

## How to Run

```bash
python run_game.py
```

Make sure your virtual environment is activated and dependencies are installed.

---

## License
This project is open for educational and non-commercial use. Modify it, expand it, and learn from it!