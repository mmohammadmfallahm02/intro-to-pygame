# Runner Game 🏃‍♂️

A fun pygame-based platformer game where you control a player character to avoid obstacles and survive as long as possible!

## Overview

**Runner** is a simple but engaging 2D platformer game built with Python and Pygame. The player must jump over incoming snail enemies to survive. The game features smooth animations, gravity mechanics, and collision detection.

## Game Features

- **Player Character**: Walk and jump mechanics with gravity physics
- **Obstacles**: Snail enemies that move across the screen
- **Graphics**: Beautiful pixel art assets for the sky, ground, player, and enemies
- **Audio**: Background music and jump sound effects
- **Smooth Gameplay**: 60 FPS frame rate for fluid gameplay

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Pygame:
```bash
pip install pygame
```

2. Navigate to the game directory:
```bash
cd /Users/mmohammadmfallahm02/python/game
```

## How to Run

```bash
python game.py
```

## Game Controls

- **SPACEBAR**: Jump to avoid obstacles
- **Click Window Close Button**: Exit the game

## Game Mechanics

- The player starts at the bottom left of the screen
- Snails move from right to left across the screen
- Jump over snails to survive
- Collision with a snail ends the game
- The game runs at 60 FPS for smooth gameplay

## File Structure

```
game/
├── game.py              # Main game file
├── audio/
│   ├── jump.mp3        # Jump sound effect
│   └── music.wav       # Background music
├── font/
│   └── Pixeltype.ttf   # Pixel-style font
└── graphics/
    ├── Sky.png         # Background sky
    ├── ground.png      # Ground platform
    ├── Player/
    │   ├── player_stand.png    # Standing animation
    │   ├── player_walk_1.png   # Walking frame 1
    │   ├── player_walk_2.png   # Walking frame 2
    │   └── jump.png            # Jumping animation
    ├── snail/
    │   ├── snail1.png          # Snail frame 1
    │   └── snail2.png          # Snail frame 2
    └── Fly/
        ├── Fly1.png            # Fly enemy frame 1
        └── Fly2.png            # Fly enemy frame 2
```

---

## Development Progress 📋

### ✅ Completed Tasks

- [x] **Core Game Loop**: Implemented main game loop with event handling
- [x] **Graphics Loading**: Load and display sky, ground, and character sprites
- [x] **Player Movement**: Implement player position and drawing
- [x] **Jump Mechanics**: Space bar to jump with gravity physics
- [x] **Player Gravity**: Realistic falling animation with gravity
- [x] **Snail Obstacles**: Create moving snail enemies from right to left
- [x] **Collision Detection**: Detect collision between player and snails
- [x] **Game Over**: Exit game on collision with enemy
- [x] **UI Display**: Show game title/score on screen with background rect
- [x] **Frame Rate Control**: Set game to run at 60 FPS for smooth gameplay
- [x] **Asset Organization**: Organize all graphics and audio files into folders
- [x] **Game Window Setup**: Create 800x400 game window with "Runner" title

### 📋 Pending Tasks (To-Do)

- [ ] **Score System**: Implement and display a score counter
- [ ] **Sound Effects**: Add jump sound when player jumps
- [ ] **Background Music**: Add background music to gameplay
- [ ] **Player Animation**: Implement walking animation frames
- [ ] **Snail Animation**: Animate snail frames while moving
- [ ] **Flying Enemy**: Add flying obstacles with different behavior
- [ ] **Difficulty Scaling**: Increase obstacle speed/frequency over time
- [ ] **High Score**: Track and display high score across game sessions
- [ ] **Pause Menu**: Add ability to pause/resume game
- [ ] **Settings Menu**: Add volume controls and display settings
- [ ] **Multiple Levels**: Create different difficulty levels
- [ ] **Power-ups**: Add temporary power-ups (invincibility, speed boost, etc.)
- [ ] **Particle Effects**: Add visual effects for jumps and collisions
- [ ] **Game States**: Implement start screen and game over screen
- [ ] **Leaderboard**: Store and display top scores
- [ ] **Mobile Support**: Adapt controls for mobile devices
- [ ] **Unit Tests**: Add test cases for game logic
- [ ] **Code Refactoring**: Organize code into classes and separate modules

---

## Known Issues 🐛

- Window title shows "Runner" but score display text shows "My game" (inconsistency)
- File path references may need updating (e.g., `Graphics/Ground.png` vs `graphics/ground.png`)
- No sound effects or background music currently playing
- No pause functionality available
- Game has no start or end screen, just runs continuously until collision

## Future Enhancements 🚀

- [ ] Mobile game version
- [ ] Leaderboard with online storage
- [ ] Different game modes (endless, timed, survival)
- [ ] Customizable character skins
- [ ] Level editor for community-created levels

---

## Credits

- **Developer**: Your Name
- **Framework**: Pygame
- **Art Assets**: Pixel art graphics
- **Font**: Pixeltype TTF font

## License

This project is open source. Feel free to modify and distribute as needed.

---

**Enjoy playing Runner! 🎮**
