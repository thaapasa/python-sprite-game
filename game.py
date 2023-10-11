import pygame
from pygame.locals import *
from defs import SCREEN_WIDTH, SCREEN_HEIGHT, CHARACTER_SPEED, WHITE
from animation_handler import AnimationHandler

# Initialize pygame
pygame.init()

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

walk_animation = AnimationHandler('sprites/walk-tileset.png', 8, 0.05) 

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
    walk_animation.set_direction(False)
    character_rect.move_ip(-CHARACTER_SPEED * dt, 0)
    walk_animation.update(dt)
  if keys[K_RIGHT]:
    walk_animation.set_direction(True)
    character_rect.move_ip(CHARACTER_SPEED * dt, 0)
    walk_animation.update(dt)

  # Drawing
  screen.fill(WHITE)
  screen.blit(walk_animation.get_current_frame(), character_rect.topleft)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
