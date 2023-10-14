import pygame
import pygame.sprite
from enum import Enum
from defs import DRAW_BBOX, RED


TILE_WIDTH = 32
TILE_HEIGHT = 32


class TileType(Enum):
    EMPTY = (" ", -1, -1)
    GROUND = ("#", 5, 5)
    TOP = ("^", 1, 0)
    BOTTOM = ("v", 8, 4)
    LEFT = ("<", 0, 1)
    RIGHT = (">", 3, 1)
    LEFT_RIGHT = ("H", 4, 1)
    TOP_LEFT = ("┌", 0, 0)
    TOP_RIGHT = ("┐", 2, 0)
    TOP_BOTTOM = ("=", 1, 4)
    BOTTOM_LEFT = ("└", 7, 4)
    BOTTOM_RIGHT = ("┘", 9, 4)
    TOP_BOTTOM_LEFT = ("├", 0, 4)
    TOP_BOTTOM_RIGHT = ("┤", 2, 4)
    TOP_RIGHT_LEFT = ("┬", 4, 0)
    BOTTOM_RIGHT_LEFT = ("┴", 8, 4)
    ALL_BORDERS = ("┼", 5, 2)

    @property
    def char(self):
        return self.value[0]

    @property
    def tile_pos(self):
        return (self.value[1], self.value[2])

    @classmethod
    def from_char(cls, char):
        return cls._lookup_map.get(char, cls.EMPTY)


TileType._lookup_map = {member.char: member for member in TileType}


class BgTile(pygame.sprite.Sprite):
    def __init__(self, tile: TileType, image: pygame.Surface, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.tile = tile
        self.rect = pygame.Rect(
            x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT
        )
        self.image = image


class LevelHandler:
    def __init__(self, level, width, height):
        self.width = width
        self.height = height
        # Setup images
        self.tiles = self._setup_tiles()
        self.level = self._load_level(level, width, height)
        self.sprites = self._create_sprites()

    def _setup_tiles(self):
        # Load background
        tileset = pygame.image.load("sprites/background-tileset.png")
        return {member.char: self._extract_tile(member, tileset) for member in TileType}

    def _create_sprites(self):
        sprites = pygame.sprite.Group()
        for y, row in enumerate(self.level):
            for x, tile in enumerate(row):
                if tile is not None and tile is not TileType.EMPTY:
                    sprites.add(BgTile(tile, self.tiles[tile.char], x, y))
        return sprites

    def _extract_tile(self, tile, tileset) -> pygame.Surface:
        pos = tile.tile_pos
        if pos[0] < 0 or pos[1] < 0:
            return pygame.Surface((32, 32), pygame.SRCALPHA)
        frame_rect = pygame.Rect(
            pos[0] * TILE_WIDTH, pos[1] * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT
        )
        return tileset.subsurface(frame_rect)

    def _load_level(self, level, width, height):
        with open(level, "r") as file:
            lines = file.readlines()

        # Create a 2D array based on the lines and characters
        level = [
            [
                TileType.from_char(char) if len(line) > col else None
                for col, char in enumerate(line)
            ]
            for line in lines
        ]

        # Pad additional rows if the level height is less than the specified height
        while len(level) < height:
            level.append([TileType.EMPTY] * width)

        # Pad additional columns in each row if the row width is less than the specified width
        for row in level:
            while len(row) < width:
                row.append(TileType.EMPTY)
        return level

    def draw(self, screen):
        self.sprites.draw(screen)
        if DRAW_BBOX:
            for tile in self.sprites:
                pygame.draw.rect(screen, RED, tile.rect, 2)
