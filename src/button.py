import pygame
import math

class Button():
    def __init__(self, x, y, image, scale, selected_frame_index=0):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.selected_frame_index = selected_frame_index

        # Create a mask based on the alpha channel
        self.alpha_mask = pygame.mask.from_surface(self.image, 127)  # 127 is the threshold for alpha values

        # self.outline_color = (255, 0, 0)  # Select an outline color
        # self.outline_width = 5  # Choose how thicc the hitbox will be

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check if the mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                # Check for collision with the alpha mask
                if self.check_alpha_collision(pos):
                    self.clicked = True
                    action = True

        # Reset click state when the mouse button is released
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        # if self.clicked:
        #     pygame.draw.rect(surface, self.outline_color, self.rect, self.outline_width)

        return action

    def check_alpha_collision(self, pos):
        # Calculate the relative position within the image
        relative_pos = (pos[0] - self.rect.x, pos[1] - self.rect.y)

        # Check if the alpha value of the pixel is greater than the threshold
        alpha_value = self.image.get_at(relative_pos).a
        return alpha_value > 127
