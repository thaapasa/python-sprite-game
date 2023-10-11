import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
CHARACTER_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Knight')

# Load character sprite
character = pygame.image.load('sprites/idle.png')
character_rect = character.get_rect()
character_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[K_LEFT]:
    character_rect.move_ip(-CHARACTER_SPEED, 0)
  if keys[K_RIGHT]:
    character_rect.move_ip(CHARACTER_SPEED, 0)

  # Drawing
  screen.fill(WHITE)
  screen.blit(character, character_rect.topleft)

  pygame.display.flip()

pygame.quit()
