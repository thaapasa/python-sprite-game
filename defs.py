from enum import Enum

# Speeds are pixels per second
WALKING_SPEED = 240
RUNNING_SPEED = 360

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

# Length, in seconds
JUMP_LENGTH = 0.4
JUMP_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)


# Direction
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
