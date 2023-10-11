import pygame
from enum import Enum


class TileType(Enum):
    EMPTY = (" ", "")
    GROUND = ("#", "ground")
    TOP = ("^", "ground-top")
    BOTTOM = ("v", "ground-b")
    LEFT = ("<", "ground-l")
    RIGHT = (">", "ground-r")
    TOP_LEFT = ("┌", "ground-tl")
    TOP_RIGHT = ("┐", "ground-tr")
    BOTTOM_LEFT = ("└", "ground-bl")
    BOTTOM_RIGHT = ("┘", "ground-br")
    TOP_BOTTOM_LEFT = ("├", "ground-tbl")
    TOP_BOTTOM_RIGHT = ("┤", "ground-tbr")
    TOP_RIGHT_LEFT = ("┬", "ground-trl")
    BOTTOM_RIGHT_LEFT = ("┴", "ground-brl")
    ALL_BORDERS = ("┼", "ground-all")

    @property
    def char(self):
        return self.value[0]

    @property
    def filename(self):
        return self.value[1]

    @classmethod
    def from_char(cls, char):
        return cls._lookup_map.get(char, cls.EMPTY)


TileType._lookup_map = {member.char: member for member in TileType}


class LevelHandler:
    def __init__(self, level, width, height):
        self.level = self._load(level, width, height)
        print("Level", self.level)

    def _load(self, level, width, height):
        with open(level, "r") as file:
            lines = file.readlines()

        # Create a 2D array based on the lines and characters
        level = [
            [
                TileType.from_char(char) if len(line) > col else TileType.EMPTY
                for col, char in enumerate(line.strip())
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
