import pygame
import pygame.sprite


def find_mtv(
    target: pygame.Rect, o: pygame.Rect, velocity: pygame.Vector2, along_x: bool
):
    """Finds minimum translation vector that moves target backwards along
    velocity so it doesn't collide with o anymore"""
    coll_box = target.clip(o)

    # Collision amount, per axis
    cx = coll_box.width
    cy = coll_box.height
    if cx == 0 and cy == 0:
        return None

    # pushback
    pb = velocity.normalize() * -1

    # Adjust direction
    if pb[0] < 0:
        cx = -cx
    if pb[1] < 0:
        cy = -cy

    return (cx, 0) if along_x else (0, cy)
