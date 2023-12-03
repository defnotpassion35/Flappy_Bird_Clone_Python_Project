import pygame
import random

screen_width = 1920
screen_height = 1080

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, height, gap):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.height = height
        self.gap = gap
        self.width = 80
        self.rect = pygame.Rect(self.x, 0, self.width, self.height)
        self.lower_rect = pygame.Rect(self.x, int(self.height + self.gap), self.width, int(screen_height - self.height - self.gap))

    def update(self, speed):
        # Move the pipe to the left
        self.x -= speed
        self.rect.x = self.x

    def offscreen(self):
        # Check if the pipe is offscreen
        return self.x + self.width < 0

    def draw(self, screen, pipe_color):
    # Draw the upper part of the pipe
        pygame.draw.rect(screen, pipe_color, (self.x, 0, self.width, int(self.height)))
    
    # Draw the lower part of the pipe
        pygame.draw.rect(screen, pipe_color, (self.x, int(self.height + self.gap), self.width, int(screen_height - self.height - self.gap)))
