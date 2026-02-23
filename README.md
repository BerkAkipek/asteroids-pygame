# Asteroids (Pygame)

A small Asteroids-style arcade game built in Python with `pygame` as part of the Boot.dev tutorial.

## Features

- Player ship movement and rotation
- Random asteroid spawning from screen edges
- Shooting with cooldown
- Asteroid splitting on hit
- Game over on player collision
- JSONL logging for game state and gameplay events

## Tech Stack

- Python 3.12+
- `pygame==2.6.1`

## Controls

- `W` - Move forward
- `S` - Move backward
- `A` - Rotate left
- `D` - Rotate right
- `Space` - Shoot
- Close window - Quit

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd asteroids-pygame
```

### 2. Install dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or with `pip`:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install pygame==2.6.1
```

### 3. Run the game

```bash
python main.py
```

## Project Structure

- `main.py` - Game loop, collision handling, rendering
- `player.py` - Player ship movement, rotation, and shooting
- `asteroid.py` - Asteroid behavior and splitting logic
- `asteroidfield.py` - Asteroid spawning system
- `shot.py` - Projectile behavior
- `circleshape.py` - Shared circular collision base class
- `constants.py` - Game tuning constants (screen size, speeds, cooldowns)
- `logger.py` - Writes debug/gameplay logs to JSONL files

## Logging

When the game runs, it creates:

- `game_state.jsonl` - periodic snapshots of entities and state
- `game_events.jsonl` - events such as `asteroid_shot`, `asteroid_split`, and `player_hit`

These files are useful for debugging and telemetry.
