import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CHARACTER_SPEED = 240 # pixels per second

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Knight')

# Load character sprite
character = pygame.image.load('sprites/idle.png')
character_rect = character.get_rect()
character_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

clock = pygame.time.Clock()
# Main game loop
running = True
while running:
  # Time since last frame
  dt = clock.get_time() / 1000.0

  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[K_LEFT]:
    character_rect.move_ip(-CHARACTER_SPEED * dt, 0)
  if keys[K_RIGHT]:
    character_rect.move_ip(CHARACTER_SPEED * dt, 0)

  # Drawing
  screen.fill(WHITE)
  screen.blit(character, character_rect.topleft)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
