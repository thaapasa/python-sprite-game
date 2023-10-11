import pygame
from pygame.locals import *
from defs import SCREEN_WIDTH, SCREEN_HEIGHT, CHARACTER_SPEED, SPRITE_WIDTH, SPRITE_HEIGHT
from animation_handler import AnimationHandler

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Knight')

# Setup character pos
character_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SPRITE_WIDTH, SPRITE_HEIGHT)  
walking = False

# Load background
background = pygame.image.load('sprites/background.png')

# Load character sprite
idle_animation = AnimationHandler('sprites/idle-tileset.png', 8, 0.07) 
walk_animation = AnimationHandler('sprites/walk-tileset.png', 8, 0.05) 

clock = pygame.time.Clock()

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
  if keys[K_LEFT]:
    walk_animation.set_direction(False)
    character_rect.move_ip(-CHARACTER_SPEED * dt, 0)
    walk_animation.update(dt)
    walking = True
  elif keys[K_RIGHT]:
    walk_animation.set_direction(True)
    character_rect.move_ip(CHARACTER_SPEED * dt, 0)
    walk_animation.update(dt)
    walking = True
  else:
    idle_animation.update(dt)
    walking = False

  # Drawing
  screen.blit(background, (0,0))
  cur_animation = walk_animation if walking else idle_animation
  screen.blit(cur_animation.get_current_frame(), character_rect.topleft)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
