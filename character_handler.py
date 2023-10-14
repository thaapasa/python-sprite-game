import pygame
from enum import Enum
from defs import (
    SPRITE_WIDTH,
    SPRITE_HEIGHT,
    WALKING_SPEED,
    RUNNING_SPEED,
    JUMP_LENGTH,
    JUMP_HEIGHT,
    DRAW_BBOX,
    BLUE,
    Direction,
)
from animation_handler import AnimationHandler
from utils import add_coordinates


class CharState(Enum):
    IDLE = 1
    WALKING = 2
    RUNNING = 3
    JUMPING = 4


class CharacterHandler:
    def __init__(self):
        self.rect = pygame.Rect(
            14 * 32 - 128, 19 * 32 - 128, SPRITE_WIDTH, SPRITE_HEIGHT
        )
        self.bbox = pygame.Rect(40, 55, SPRITE_WIDTH - 80, SPRITE_HEIGHT - 55)

        # Load animations
        self.idle_animation = AnimationHandler("sprites/idle-tileset.png", 8, 0.07)
        self.walk_animation = AnimationHandler("sprites/walk-tileset.png", 8, 0.05)
        self.run_animation = AnimationHandler("sprites/run-tileset.png", 8, 0.04)
        self.jump_animation = AnimationHandler(
            "sprites/jump-tileset.png", 8, JUMP_LENGTH / 8
        )

        self.state = CharState.IDLE
        self.state_anims = {
            CharState.IDLE: self.idle_animation,
            CharState.WALKING: self.walk_animation,
            CharState.RUNNING: self.run_animation,
            CharState.JUMPING: self.jump_animation,
        }
        self.direction = Direction.RIGHT

        self.jump_timer = 0
        self.jump_speed = WALKING_SPEED
        self.jump_start = (0, 0)

    def walk(self, direction):
        if self.state is CharState.JUMPING:
            return
        self.direction = direction
        if self.state is not CharState.WALKING:
            self.state = CharState.WALKING
            self.walk_animation.reset()

    def run(self, direction):
        if self.state is CharState.JUMPING:
            return
        self.direction = direction
        if self.state is not CharState.RUNNING:
            self.state = CharState.RUNNING
            self.run_animation.reset()

    def idle(self):
        if self.state is CharState.JUMPING:
            return
        if self.state is not CharState.IDLE:
            self.state = CharState.IDLE
            self.idle_animation.reset()

    def jump(self):
        if self.state is CharState.WALKING:
            self.jump_speed = WALKING_SPEED
        elif self.state is CharState.RUNNING:
            self.jump_speed = RUNNING_SPEED
        else:
            return
        self.state = CharState.JUMPING
        self.jump_timer = 0
        self.jump_start = self.rect.topleft
        self.jump_animation.reset()

    def update(self, dt):
        self.state_anims[self.state].update(dt)
        dir_mult = 1 if self.direction is Direction.RIGHT else -1
        if self.state is CharState.WALKING:
            self.rect.move_ip(WALKING_SPEED * dt * dir_mult, 0)
        elif self.state is CharState.RUNNING:
            self.rect.move_ip(RUNNING_SPEED * dt * dir_mult, 0)
        elif self.state is CharState.JUMPING:
            self._calc_jump(dt)

    def _calc_jump(self, dt):
        self.jump_timer += dt
        dir_mult = 1 if self.direction is Direction.RIGHT else -1
        # Position in jump (0 to 1)
        p = self.jump_timer / JUMP_LENGTH

        if p >= 1:
            # Jump complete, reset to idle
            self.rect.topleft = (
                self.jump_start[0] + JUMP_LENGTH * self.jump_speed * dir_mult,
                self.jump_start[1],
            )
            self.state = CharState.IDLE
        else:
            x_offs = self.jump_timer * self.jump_speed * dir_mult
            y_offs = 4 * JUMP_HEIGHT * p * (1 - p)
            self.rect.topleft = (
                self.jump_start[0] + x_offs,
                self.jump_start[1] - y_offs,
            )

    def draw(self, screen):
        screen.blit(
            self.state_anims[self.state].get_current_frame(
                self.direction is Direction.RIGHT
            ),
            self.rect.topleft,
        )
        if DRAW_BBOX:
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    add_coordinates(self.rect.topleft, self.bbox.topleft),
                    (self.bbox.width, self.bbox.height),
                ),
                2,
            )
