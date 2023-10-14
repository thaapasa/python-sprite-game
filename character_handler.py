import pygame
import pygame.sprite
from enum import Enum
from defs import (
    SPRITE_WIDTH,
    SPRITE_HEIGHT,
    WALKING_SPEED,
    RUNNING_SPEED,
    DRAW_BBOX,
    JUMP_VELOCITY,
    MAX_VELOCITY_Y,
    BLUE,
    GRAVITY,
    Direction,
)
from animation_handler import AnimationHandler
from collision import find_mtv
from utils import add_coordinates


class CharState(Enum):
    IDLE = 1
    WALKING = 2
    RUNNING = 3
    JUMPING = 4


BBOX_WIDTH = 42
BBOX_HEIGHT = 74


DIR_MULT = {Direction.LEFT: -1, Direction.RIGHT: 1}


class CharacterHandler(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # rect is the bounding box
        self.rect = pygame.Rect(
            x - BBOX_WIDTH / 2, y - BBOX_HEIGHT, BBOX_WIDTH, BBOX_HEIGHT
        )
        self.sprite_offs = (
            BBOX_WIDTH / 2 - SPRITE_WIDTH / 2,
            -(SPRITE_HEIGHT - BBOX_HEIGHT),
        )
        self.velocity_x = 0
        self.velocity_y = 0

        self.grounded = True

        # Load animations
        self.idle_animation = AnimationHandler("sprites/idle-tileset.png", 8, 0.07)
        self.walk_animation = AnimationHandler("sprites/walk-tileset.png", 8, 0.05)
        self.run_animation = AnimationHandler("sprites/run-tileset.png", 8, 0.04)
        self.jump_animation = AnimationHandler(
            "sprites/jump-tileset.png", 8, 0.07, loop=False
        )

        self.state = CharState.IDLE
        self.state_anims = {
            CharState.IDLE: self.idle_animation,
            CharState.WALKING: self.walk_animation,
            CharState.RUNNING: self.run_animation,
            CharState.JUMPING: self.jump_animation,
        }

    def walk(self, direction: Direction):
        self.velocity_x = DIR_MULT[direction] * WALKING_SPEED
        if self.state is not CharState.WALKING and self.state is not CharState.JUMPING:
            self.state = CharState.WALKING
            self.walk_animation.reset()

    def run(self, direction):
        self.velocity_x = DIR_MULT[direction] * RUNNING_SPEED
        if self.state is not CharState.RUNNING and self.state is not CharState.JUMPING:
            self.state = CharState.RUNNING
            self.run_animation.reset()

    def idle(self):
        self.velocity_x = 0
        if self.state is not CharState.IDLE and self.state is not CharState.JUMPING:
            self.state = CharState.IDLE
            self.idle_animation.reset()

    def jump(self):
        if self.state is not CharState.JUMPING:
            self.velocity_y -= JUMP_VELOCITY
            self.state = CharState.JUMPING
            self.jump_animation.reset()

    def update(self, dt, level):
        self.grounded = False
        self.state_anims[self.state].update(dt)
        self.velocity_y += min(GRAVITY * dt, MAX_VELOCITY_Y)
        self.rect.move_ip(self.velocity_x * dt, self.velocity_y * dt)
        self._check_collision(level)
        if self.state == CharState.JUMPING and self.grounded:
            self.state = CharState.IDLE

    def _check_collision(self, level):
        collisions = pygame.sprite.spritecollide(self, level.sprites, False)
        for c in collisions:
            self._resolve_collision(c)

    def velocity(self) -> pygame.Vector2:
        if self.velocity_x == 0 and self.velocity_y == 0:
            return pygame.Vector2(0, GRAVITY)
        return pygame.Vector2(self.velocity_x, self.velocity_y)

    def _resolve_collision(self, sprite: pygame.sprite.Sprite):
        adj = find_mtv(self.rect, sprite.rect, self.velocity())
        if not adj:
            return

        self.rect.move_ip(adj)
        self.velocity_y = 0
        self.grounded = True

    def draw(self, screen):
        screen.blit(
            self.state_anims[self.state].get_current_frame(self.velocity_x >= 0),
            add_coordinates(self.rect.topleft, self.sprite_offs),
        )
        if DRAW_BBOX:
            pygame.draw.rect(screen, BLUE, self.rect, 2)
