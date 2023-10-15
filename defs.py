from enum import Enum


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
