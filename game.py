import pygame
from pygame.locals import *
from defs import SCREEN_WIDTH, SCREEN_HEIGHT, Direction
from character_handler import CharacterHandler

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Knight")

# Load background
background = pygame.image.load("sprites/background.png")

clock = pygame.time.Clock()

char = CharacterHandler()

# Main game loop
game_running = True
while game_running:
    # Time since last frame
    dt = clock.get_time() / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_q or event.key == K_ESCAPE:
                game_running = False

    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    if keys[K_LEFT]:
        if mods & KMOD_SHIFT:
            char.run(Direction.LEFT)
        else:
            char.walk(Direction.LEFT)
    elif keys[K_RIGHT]:
        if mods & KMOD_SHIFT:
            char.run(Direction.RIGHT)
        else:
            char.walk(Direction.RIGHT)
    else:
        char.idle()

    char.update(dt)

    # Drawing
    screen.blit(background, (0, 0))
    char.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
