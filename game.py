import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CHARACTER_SPEED = 240 # pixels per second

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Knight')

# Load character sprite
character = pygame.image.load('sprites/idle.png')
character_rect = character.get_rect()
character_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Load the sprite sheet
walk_sheet = pygame.image.load('sprites/walk-tileset.png')

walk_frames = []
reverse_walk_frames = []

for x in range(8):
  frame_rect = pygame.Rect(x * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
  frame_image = walk_sheet.subsurface(frame_rect)
  walk_frames.append(frame_image)
  flipped_image = pygame.transform.flip(frame_image, True, False)
  reverse_walk_frames.append(flipped_image)

goingRight = True
clock = pygame.time.Clock()
# Main game loop
running = True
walkFrame = 0
while running:
  # Time since last frame
  dt = clock.get_time() / 1000.0

  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    elif event.type == KEYDOWN:
      if event.key == K_q or event.key == K_ESCAPE:
        running = False      

  keys = pygame.key.get_pressed()
  if keys[K_LEFT]:
    character_rect.move_ip(-CHARACTER_SPEED * dt, 0)
    walkFrame += 1
    walkFrame %= 8
    goingRight = False
  if keys[K_RIGHT]:
    character_rect.move_ip(CHARACTER_SPEED * dt, 0)
    walkFrame += 1
    walkFrame %= 8
    goingRight = True

  # Drawing
  screen.fill(WHITE)
  screen.blit((walk_frames if goingRight else reverse_walk_frames)[walkFrame], character_rect.topleft)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
