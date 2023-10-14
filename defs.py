from enum import Enum

# Speeds are pixels per second
WALKING_SPEED = 240
RUNNING_SPEED = 360
JUMP_VELOCITY = 500
GRAVITY = 1500
MAX_VELOCITY_Y = 1200

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


# Direction
class Direction(Enum):
    RIGHT = 1
    LEFT = 2


DRAW_BBOX = False
