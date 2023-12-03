import pygame
import os

class FlappyBird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Bird location
        self.x = x
        self.y = y

        # Bird movement attributes
        self.Y_velocity = -125
        self.gravity = 5

        # Bird image and rect
        cwd = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(cwd, "img", "plane.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def flap(self):
        # Implement the bird's jump action
        print("the bird is flapping")
        self.rect.y += self.Y_velocity

    def update(self, screen_height):
        # Implement the bird's movement (gravity)
        self.rect.y += self.gravity
        #print("current y position: self.rect.y: " + str(self.rect.y))

        # Limit to not allow bird to move out of the screen (vertically)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, screen):
        screen.blit(self.image, self.rect)