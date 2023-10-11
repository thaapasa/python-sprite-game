import pygame
from enum import Enum
from defs import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SPRITE_WIDTH,
    SPRITE_HEIGHT,
    WALKING_SPEED,
    RUNNING_SPEED,
    Direction,
)
from animation_handler import AnimationHandler


class CharState(Enum):
    IDLE = 1
    WALKING = 2
    RUNNING = 3
    JUMPING = 4


class CharacterHandler:
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, SPRITE_WIDTH, SPRITE_HEIGHT
        )

        # Load animations
        self.idle_animation = AnimationHandler("sprites/idle-tileset.png", 8, 0.07)
        self.walk_animation = AnimationHandler("sprites/walk-tileset.png", 8, 0.05)
        self.run_animation = AnimationHandler("sprites/run-tileset.png", 8, 0.04)
        self.jump_animation = AnimationHandler("sprites/jump-tileset.png", 8, 0.05)

        self.state = CharState.IDLE
        self.state_anims = {
            CharState.IDLE: self.idle_animation,
            CharState.WALKING: self.walk_animation,
            CharState.RUNNING: self.run_animation,
            CharState.JUMPING: self.jump_animation,
        }
        self.direction = Direction.RIGHT

    def walk(self, direction):
        self.direction = direction
        if self.state is not CharState.WALKING:
            self.state = CharState.WALKING
            self.walk_animation.reset()

    def run(self, direction):
        self.direction = direction
        if self.state is not CharState.RUNNING:
            self.state = CharState.RUNNING
            self.run_animation.reset()

    def idle(self):
        if self.state is not CharState.IDLE:
            self.state = CharState.IDLE
            self.idle_animation.reset()

    def update(self, dt):
        self.state_anims[self.state].update(dt)
        dir_mult = 1 if self.direction is Direction.RIGHT else -1
        if self.state is CharState.WALKING:
            self.rect.move_ip(WALKING_SPEED * dt * dir_mult, 0)
        elif self.state is CharState.RUNNING:
            self.rect.move_ip(RUNNING_SPEED * dt * dir_mult, 0)

    def draw(self, screen):
        screen.blit(
            self.state_anims[self.state].get_current_frame(
                self.direction is Direction.RIGHT
            ),
            self.rect.topleft,
        )
