import pygame
import sys
import random
from bird import FlappyBird 
from bird import Bird1
from bird import Bird2
from bird import Bird3
from pipe import Pipe
import math
from button import Button

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()

        # Set up the screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Flappy Bird")

        # Set up colors 
        self.GRAY = (128, 128, 128)

        # Set up clock
        self.clock = pygame.time.Clock()

        # Create sprite groups
        self.birds = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()

        # Set up the bird
        self.bird = Bird2(screen_width // 4, screen_height // 2, "plane.png")  # Initial position
        self.birds.add(self.bird)

        # Set up pipes
        self.pipe_gap = 300
        self.pipe_spawn_frequency = 80  # in frames
        self.pipe_spawn_timer = 0
        
        # Set up Score
        self.score = 0
        self.font = pygame.font.Font(None, 36)

        # Set up game_over screen
        self.game_over = False
        self.game_over_screen = GameOver(self.screen, self.screen_width, self.screen_height)
        # Set up a Paused Screen
        self.game_paused = False

        #load bg image
        self.og_bg_img = pygame.image.load("src/img/MenuBackground.png").convert()
        self.bg_width = self.og_bg_img.get_width()
        self.scroll = 0
        self.tiles = math.ceil(screen_width / self.bg_width) + 2

    def BackGround(self):
        #Draw bg img and change dimension
        for i in range(0, self.tiles):
            self.screen.blit(self.og_bg_img, (i * self.bg_width + self.scroll, 0))

        #Scroll background
        self.scroll -= 1.5

        #Reset scroll
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

    def run(self):
        # Game loop
        while not self.game_over:
            for event in pygame.event.get()  :
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()
            
        
            # Update bird
            if not self.game_over:
                self.bird.update(self.screen_height)
                
                # Update the pipes
                speed = 5  # Set a constant speed
                self.pipes.update(speed)

            # Spawn pipes
            self.pipe_spawn_timer += 1
            if self.pipe_spawn_timer == self.pipe_spawn_frequency:
                pipe_height = random.randint(200, 600)
                new_pipe = Pipe(self.screen_width, pipe_height, self.pipe_gap)
                self.pipes.add(new_pipe)
                self.pipe_spawn_timer = 0

            # Remove offscreen pipes
            for pipe in self.pipes:
                if pipe.offscreen():
                    self.pipes.remove(pipe)

            # Check for collisions with pipes
            for pipe in self.pipes:
                if self.bird.rect.x < pipe.x + pipe.width and self.bird.rect.x + self.bird.rect.width > pipe.x:
                    if self.bird.rect.y < pipe.height or self.bird.rect.y + self.bird.rect.height > pipe.height + pipe.gap:
                        self.game_over = True
                        print("Ouch! You hit a pipe!")
               
            # Draw BG
            self.BackGround()
            
            #increasing score
            for pipe in self.pipes :
                if self.bird.x == pipe.x  + 80:  #and not game_over:
                    self.score += 1
                    print(self.score)

            # Draw pipes first
            for pipe in self.pipes:
                pipe.draw(self.screen, self.GRAY)  # Pass the pipe color

            # Draw bird last
            self.bird.draw(self.screen)
            
            # Display score
            if(self.game_over == False):
                text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
                self.screen.blit(text, (200, 70))
                
            pygame.display.flip()
            
            # Cap the frame rate
            self.clock.tick(60)  # Adjust as needed
            
        self.game_over_screen.game_over_screen(x_position=0,y_position=0)

class GameOver:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_paused = False  # Initialize game_paused attribute
        self.main_menu = None
        self.game_instance = None

        # Load button images
        start_img = pygame.image.load('src/img/PHstart_button.png').convert_alpha()
        exit_img = pygame.image.load('src/img/PHexit_button.png').convert_alpha()
        backmenu_img = pygame.image.load('src/img/back_menu.png').convert_alpha()

        # Create button instances using your custom Button class
        self.start_button = Button(50, 50, start_img, 1)  # Adjust coordinates
        self.end_button = Button(50, 150, exit_img, 1)  # Adjust coordinates
        self.backmenu_button = Button(304, 680, backmenu_img, 1)

    def game_over_screen(self, x_position, y_position):
        print(self.screen_width, self.screen_height)
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))

        x_position = 100
        y_position = 200
        text_rect = text.get_rect(topleft=(x_position, y_position))  # define the dimension
        self.screen.blit(text, text_rect)

        # Draw buttons and handle events
        in_game_over_screen = True

        while in_game_over_screen:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        in_game_over_screen = False  # Break the loop on spacebar press
                        self.restart_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.draw(self.screen):
                        self.restart_game()
                    elif self.backmenu_button.draw(self.screen):
                        self.return_menu()
                    elif self.end_button.draw(self.screen):
                        pygame.quit()
                        sys.exit()
            # Draw buttons outside the event loop
            self.start_button.draw(self.screen)
            self.end_button.draw(self.screen)
            self.backmenu_button.draw(self.screen)

            pygame.display.flip()

    def restart_game(self):
        from main_menu import Menu
        self.game_instance = Game(1920, 1080)  # Create a new Game instance
        self.game_instance.run()
    def return_menu(self):
        from main_menu import Menu
        self.main_menu = Menu(self.screen, screen_height= 1080 , screen_width= 1920)
        self.main_menu.run()
    # Loop
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_paused = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    game = Game(1920, 1080)
    game.run()
    pygame.quit()

