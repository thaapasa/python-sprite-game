import pygame

from defs import SPRITE_WIDTH, SPRITE_HEIGHT


class AnimationHandler:
    def __init__(self, tileset_path, frame_count, frame_duration):
        self.tileset = pygame.image.load(tileset_path)
        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.elapsed_time = 0

        self.frames = []
        self.frames_reverse = []

        # Generate frame images
        for x in range(frame_count):
            frame_rect = pygame.Rect(x * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
            frame_image = self.tileset.subsurface(frame_rect)
            self.frames.append(frame_image)
            flipped_image = pygame.transform.flip(frame_image, True, False)
            self.frames_reverse.append(flipped_image)

    def update(self, dt):
        """Update the animation based on elapsed time."""
        self.elapsed_time += dt
        while self.elapsed_time >= self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.elapsed_time -= self.frame_duration

    def reset(self):
        self.current_frame = 0

    def get_current_frame(self, forward):
        """Return the current frame as a Surface."""
        frames = self.frames if forward else self.frames_reverse
        return frames[self.current_frame]
