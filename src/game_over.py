import pygame
import sys
from button import Button 
from game import Game

class GameOver:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_paused = False  # Initialize game_paused attribute
        self.main_menu = "main_menu"
        self.game_instance = None
        # Load button images
        start_img = pygame.image.load('src/img/start_button.png').convert_alpha()
        exit_img = pygame.image.load('src/img/exit_button.png').convert_alpha()
        backmenu_img = pygame.image.load('src/img/back_menu.png').convert_alpha()
        
        # Create button instances using your custom Button class
        self.start_button = Button(50, 50, start_img, 0.25)  # Adjust coordinates
        self.end_button = Button(50, 150, exit_img, 0.25)  # Adjust coordinates
        self.backmenu_button = Button(304, 680, backmenu_img, 0.25)
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
                    if event.key == pygame.K_SPACE:
                        in_game_over_screen = False  # Break the loop on spacebar press
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.draw(self.screen):
                        print("Start button clicked")  # Add your start button logic here
                    elif self.end_button.draw(self.screen):
                        pygame.quit()
                        sys.exit()
            #Check for Quit Button
            if self.game_paused:
                    #check menu_state
                    if self.menu_state == "main_menu":
                        #draw pause screen buttons
                        if self.start_button.draw(self.screen):
                            self.game_paused = False
                            game = Game(1920, 1080) #Create a Game instance
                            game.run()
                        if self.end_button.draw(self.screen):
                            run = False
            # Draw buttons outside the event loop
            self.start_button.draw(self.screen)
            self.end_button.draw(self.screen)

            pygame.display.flip()

            
    #Loop
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_paused = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
