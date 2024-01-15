import pygame
import random

screen_height = 1080
screen_width = 1920

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, height, gap):
        pygame.sprite.Sprite.__init__(self)
        self._x = x  # Protected attributes
        self._height = height
        self._gap = gap
        self._width = 80
        self.rect = pygame.Rect(self._x, 0, self._width, self._height)
        self.lower_rect = pygame.Rect(
            self._x,
            int(self._height + self._gap),
            self._width,
            int(screen_height - self._height - self._gap),
        )

        # Load custom pipe image
        self.pipe_image = pygame.image.load("src/img/SimpleStyle1.png").convert_alpha()

    def get_x(self):
        return self._x

    def get_height(self):
        return self._height

    def get_gap(self):
        return self._gap

    def get_width(self):
        return self._width

    def update(self, speed):
        # Move the pipe to the left
        self._x -= speed
        self.rect.x = self._x

    def offscreen(self):
        # Check if the pipe is offscreen
        return self._x + self._width < 0

    def draw(self, screen):
        # Draw the custom pipe image
        screen.blit(self.pipe_image, (self._x, 0))