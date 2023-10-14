import pygame
from collision import find_mtv


p = pygame.Rect(5, 7, 5, 4)


def test_mtv():
    assert find_mtv(p, pygame.Rect(7, 10, 5, 5), pygame.Vector2(1, 2)) == (-0.5, -1)
    assert find_mtv(p, pygame.Rect(7, 10, 5, 5), pygame.Vector2(0, 2)) == (0, -1)
    assert find_mtv(p, pygame.Rect(9, 5, 4, 4), pygame.Vector2(3, 0)) == (-1, 0)
    assert find_mtv(p, pygame.Rect(9, 5, 4, 4), pygame.Vector2(0, -1)) == (0, 2)
    assert find_mtv(p, pygame.Rect(4, 5, 4, 3), pygame.Vector2(0, -1)) == (0, 1)
    assert find_mtv(p, pygame.Rect(4, 5, 4, 3), pygame.Vector2(-2, 0)) == (3, 0)


def test_problem():
    assert find_mtv(
        pygame.Rect(272, 567, 48, 74),
        pygame.Rect(256, 640, 32, 32),
        pygame.Vector2(240, 0),
    ) == (0, -1)
