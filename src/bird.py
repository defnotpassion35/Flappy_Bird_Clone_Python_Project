import pygame
import os

class FlappyBird(pygame.sprite.Sprite):
    #still have to add image and sound into init
    
    #DECLARE VARIABLE   
    x = None
    y = None
    img_string = None
        
    #CONSTRUCOTRS
    def __init__(self, x, y, sprite_images_paths, num_frames, scale_factor=3.5): #, img_string
        # Initialize attributes for the bird
        pygame.sprite.Sprite.__init__(self)
        
        #Bird (Initial) lOcation
        self.x = x  
        self.y = y 
        self.num_frames = num_frames
        self.index = 0
        self.counter = 0
        # self.img_string = img_string
        
        #Bird movement attribute
        self.Y_velocity = -100
        self.gravity = 5
        
        #self.sound[collide]
        
        #adding image
        cwd = os.path.dirname(__file__)
        self.sprite_images = pygame.image.load(os.path.join(cwd, "img", sprite_images_paths))
        self.frame_width = self.sprite_images.get_width() // num_frames
        self.frame_height = self.sprite_images.get_height()
        self.frames = [pygame.transform.scale(
            self.sprite_images.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
            (int(self.frame_width * scale_factor), int(self.frame_height * scale_factor)))
            for i in range(num_frames)] #Scale and add frame to the sprite
        
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def flap(self):
        # Implement the bird's jump action
        print("the bird is flapping")
        self.rect.y += self.Y_velocity

    def update(self, screen_height):
        # Implement the bird's movement (gravity + horizontal)
        self.rect.y += self.gravity
        #print("current y position: self.rect.y: " + str(self.rect.y))

        # Limit to not allow bird to move out of the screen (vertically)
        if self.rect.top < 0:
            self.rect.top = 0
            #we could possibly kill the bird or just not allow them to not go pass the border
                #self.Y_velocity = 0
                #self.gravity =  0
            # we chosse the second one here
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def animate(self):
        self.counter += 1
        if self.counter %10 == 0:
            self.index = (self.index +1) % self.num_frames
            self.image = self.frames[self.index]
            self.rect = self.image.get_rect(center=self.rect.center)
        
class Bird1(FlappyBird):
    def __init__(self, x, y, sprite_images_paths, num_frames, scale_factor=3.5):
        super().__init__(x, y, sprite_images_paths, num_frames, scale_factor)
        #adding image
        cwd = os.path.dirname(__file__)
        self.sprite_images = pygame.image.load(os.path.join(cwd, "img", "Bird_1.png"))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def flap(self):
        print("the bird is flapping 1 time faster")
        self.rect.y += 1 * self.Y_velocity
        
        
class Bird2(FlappyBird):
    def __init__(self, x, y, sprite_images_paths, num_frames, scale_factor=3.5):
        super().__init__(x, y, sprite_images_paths, num_frames, scale_factor)

        #adding image
        cwd = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(cwd, "img", "Bird_2.png")) #, imagePath))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def flap(self):
        print("the bird is flapping 1.5 time faster")
        self.rect.y += 1.5 * self.Y_velocity
        
class Bird3(FlappyBird):
    def __init__(self, x, y, sprite_images_paths, num_frames, scale_factor=3.5):
        super().__init__(x, y, sprite_images_paths, num_frames, scale_factor)

        #adding image
        cwd = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(cwd, "img", "Bird_3.png")) #, imagePath))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def flap(self):
        print("the bird is flapping 2 time faster")
        self.rect.y += 2 * self.Y_velocity

