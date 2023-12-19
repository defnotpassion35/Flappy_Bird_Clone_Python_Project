import pygame
import sys

class GameOver():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def game_over_screen(self):
        print(self.screen_width, self.screen_height)
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Display the "Game Over" screen for 2 seconds
        pygame.quit()
        sys.exit()
 


    # def draw_game_over_text(self, text, x, y):
    #     img = self.font.render(text, True, self.text_col)
    #     self.screen.blit(img, (x,y))

    # def handle_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.key_r:
    #                 return "restart"
    #         if event.type == pygame.quit:
    #             pygame.quit()
    #             quit()
    # def run(self):
    #     run = True
    #     while run:
    #         self.screen.fill(202, 228, 241)

    #        #check if the option menu is open
    #         if self.menu_state == "options":
    #             #draw different option buttons in the screen
    #             if self.video_button.draw(self.screen):
    #                     print("Video seting button is clicked")
    #             if self.backmenu_button.draw(self.screen):
    #                     self.menu_state = "main_menu"  
    #             #check if the selection screen is open
    #         if self.menu_state == "selection":
    #                 #draw other buttons for selection screen
    #             if self.backmenu_button.draw(self.screen):
    #                     self.menu_state = "main_menu"
    #     else:

    #         self.draw_game_over_text()
    #         pygame.display.update()

    #         for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
    #                 return "restart"
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 quit()
        
    
 