from enum import Enum

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WALKING_SPEED = 240  # pixels per second

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

# Colors
WHITE = (255, 255, 255)


# Direction
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
