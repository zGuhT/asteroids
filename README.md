# ThomAsteroids the Tank Engine (Python / Pygame)
<!-- Built as part of a personal assignment to refresh and rebuild foundational coding skills -->

![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A classic-style arcade **Asteroids** game clone built using **Pygame**.  
This game was originally built as part of a self-guided assignment to help refresh my coding knowledge and re-engage with Python development.  
It now features custom graphics, music, sound effects, power-ups, bombs, and a full suite of arcade gameplay improvements.

---

## Features

- Thomas the Tank Engine theme (sprites, backgrounds, music, SFX)
- Title screen with custom background and start/quit keys
- Player-controlled train with rotation, thrust, and acceleration
- Bullet shooting (coal projectiles with sound and cooldown)
- Bomb mechanic (press `B` to destroy all asteroids on screen)
- Asteroid field generation and edge spawning
- Asteroids look like bubbles and split into smaller fragments when shot, with colorful explosions
- All moving objects (player, asteroids, shots, upgrades) wrap around screen edges
- Upgrade bubbles for shield, speed boost, and rapid fire (with countdown and glow effects)
- Scoring system:
  - +1 point per second survived
  - +10 points per small asteroid destroyed
- Persistent high score saving to `data/highscore.txt`
- 3 lives with heart icons and on-death respawning
- Temporary invincibility with flashing/shimmering effect after respawn or shield powerup
- Boost and bomb UI: countdowns and bomb count in-game
- Sound effects for shooting, popping bubbles, picking up boosts, and using bombs
- Game over screen with score, high score, restart, and quit options
- Hotkey to quit (`Q` or `ESC`) at any point

---

## Controls

| Key         | Action                           |
|-------------|----------------------------------|
| W / Up      | Move forward                     |
| S / Down    | Move backward                    |
| A / D       | Rotate left/right                |
| SPACE       | Shoot coal                       |
| B           | Use bomb (clears asteroids)      |
| R           | Restart (after game over)        |
| Q / ESC     | Quit game (any time)             |

---

## Screenshots

![Screenshot](assets/screenshot1.png)
![Screenshot](assets/screenshot2.png)

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

```bash
astroids/
├── assets/                    # images, sprites, sound effects, music
│   ├── heart.png
│   ├── player_thomas.png
│   ├── background_music_thomas.mp3
│   ├── snd_shoot.wav
│   ├── snd_pop.wav
│   ├── snd_boost.wav
│   ├── snd_bomb.wav
│   ├── title_background_thomas.png
│   └── ... (other assets)
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
│   ├── functions.py
│   ├── upgradebubble.py
│   └── explosion.py
├── .gitignore
├── README.md
├── requirements.txt
└── run_game.py                # Main game entry point
```

---

## High Score System
- High scores are saved to data/highscore.txt.
- Automatically updated if you beat the previous record.

---

## Change Log

### v2.1 (2025-05-17)
- v2.1 executable created - all done i think

### v2.04 (2025-05-17)
- v2.04 fixed readme

### v2.03 (2025-05-17)
- v2.03 fixed readme

### v2.02 (2025-05-17)
- v2.02 fixed crash bug

### v2.01 (2025-05-17)
- v2.01 cleaned up some of the redundant code and added commenting to explain all the blocks

### v2.0 (2025-05-17)
- v2.0 ThomAsteroids - huge update, see readme for all features

### v1.5 (2025-05-17)
- v1.5 thomasteroids - changed to thomas the tank theme, added explosion effects and some player acceleration

### v1.3 (2025-05-17)
- v1.3 asteroids added explosion effect and heart image for remaining lives

### v1.212001 (2025-05-16)
- G: v1.212001 updated readme AGAIN again (i swear this is the last)

### v1.212 (2025-05-16)
- G: v1.212 updated readme AGAIN again

### v1.211 (2025-05-16)
- G: v1.211 updated readme AGAIN

### v1.21 (2025-05-16)
- G: v1.21 updated readme

### v1.2 (2025-05-16)
- Added update_changelog.py script for automated changelog generation and Git integration

### v1.11 (2025-05-16)
- Restructured project folders for clarity and scalability
- Added README.md and .gitignore

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
- Want more difficulty? Decrease ASTEROID_SPAWN_RATE in constants.py
- Want faster action? Adjust PLAYER_SPEED or PLAYER_SHOOT_COOLDOWN
- Add or edit power-ups in upgradebubble.py for more effects

---

## How to Run

bash
python run_game.py


Make sure your virtual environment is activated and dependencies are installed.

---

## License
This project is open for educational and non-commercial use. Modify it, expand it, and learn from it!"