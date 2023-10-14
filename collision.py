import pygame
import pygame.sprite


def find_mtv(target: pygame.Rect, o: pygame.Rect, velocity: pygame.Vector2):
    coll_box = target.clip(o)

    cx = coll_box.width
    cy = coll_box.height
    if cx == 0 and cy == 0:
        return None

    if target.centerx < o.centerx:
        cx = -cx
    if target.centery < o.centery:
        cy = -cy

    # pushback
    pb = velocity.normalize() * -1

    if pb[1] == 0 and abs(cx / cy) > 5:
        return (0, cy)

    if pb.x == 0:
        return (0, cy)
    if pb.y == 0:
        return (cx, 0)

    adj = (cx, cx * pb[1] / pb[0])
    if abs(adj[1]) > abs(cy):
        adj = (cy * pb[0] / pb[1], cy)
    return adj
