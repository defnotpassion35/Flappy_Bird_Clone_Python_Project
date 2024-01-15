import pygame
import sys
import random
import math
from button import Button
from bird import Bird1, Bird2, Bird3
from pipe import Pipe

class Game:
    def __init__(self, screen_width, screen_height, menu=None, selected_character=None):
        pygame.init()

        # Set up the screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Flappy Bird")
        self.menu = menu

        # Set up colors
        self.GRAY = (128, 128, 128)

        # Set up clock
        self.clock = pygame.time.Clock()

        # Create sprite groups
        self.birds = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()

        # Use Selected Character
        self.selected_character = selected_character
        if self.selected_character:
            # Create the bird based on the selected character
            self.bird = self.selected_character(
                screen_width // 4, screen_height // 2, num_frames=4
            )
        else:
            self.bird = Bird1(screen_width // 4, screen_height // 2, num_frames=4)

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
        self.game_over_screen = GameOver(
            self.screen, self.screen_width, self.screen_height, self
        )

        # Load bg image
        self.og_bg_img = pygame.image.load("src/img/MenuBackground.png").convert()
        self.bg_width = self.og_bg_img.get_width()
        self.scroll = 0
        self.tiles = math.ceil(screen_width / self.bg_width) + 2

        # Load custom pipe image
        self.custom_pipe_img = pygame.image.load("src/img/SimpleStyle1.png").convert_alpha()

    def draw_background(self):
        # Draw bg img and change dimension
        for i in range(0, self.tiles):
            self.screen.blit(self.og_bg_img, (i * self.bg_width + self.scroll, 0))

        # Scroll background
        self.scroll -= 1.0

        # Reset scroll 
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

    def update_objects(self):
        if not self.game_over:
            self.bird.update(self.screen_height)

            # Update the pipes
            speed = 5  # Set a constant speed
            self.pipes.update(speed)

        # Spawn pipes
        self.pipe_spawn_timer += 1
        if self.pipe_spawn_timer == self.pipe_spawn_frequency:
            new_pipe = Pipe(self.screen_width, self.custom_pipe_img, self.pipe_gap)
            self.pipes.add(new_pipe)
            self.pipe_spawn_timer = 0

        # Remove offscreen pipes
        self.pipes = pygame.sprite.Group(
            pipe for pipe in self.pipes if not pipe.offscreen()
        )

        # Check for collisions with pipes
        for pipe in self.pipes:
            if (
                self.bird.rect.x < pipe.get_x() + pipe.custom_pipe_img.get_width()
                and self.bird.rect.x + self.bird.rect.width > pipe.get_x()
                and (
                    self.bird.rect.y < pipe.custom_pipe_img.get_height()
                    or self.bird.rect.y + self.bird.rect.height
                    > pipe.custom_pipe_img.get_height() + pipe.get_gap()
                )
            ):
                self.game_over = True
                print("Ouch! You hit a pipe!")

        # Increasing score
        for pipe in self.pipes:
            if self.bird.x == pipe.get_x() + 80:
                self.score += 1
                print(self.score)

    def draw_objects(self):
        # Draw BG
        self.draw_background()

        # Draw pipes first
        for pipe in self.pipes:
            pipe.draw(self.screen)  # Pass the pipe color

        # Draw bird last
        self.bird.draw(self.screen)

        # Display score
        if not self.game_over:
            text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
            self.screen.blit(text, (200, 70))

        pygame.display.flip()

    def run(self):
        # Game loop
        while not self.game_over:
            self.handle_events()
            self.update_objects()
            self.draw_objects()

            # Cap the frame rate
            self.clock.tick(60)  # Adjust as needed

        self.game_over_screen.show_game_over_screen()


class GameOver:
    def __init__(self, screen, screen_width, screen_height, game_instance):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_instance = game_instance

        # Load button images
        start_img = pygame.image.load("src/img/start_button.png").convert_alpha()
        exit_img = pygame.image.load("src/img/exit_button.png").convert_alpha()
        backmenu_img = pygame.image.load("src/img/back_menu.png").convert_alpha()

        # Create button instances using your custom Button class
        self.start_button = Button(860, 450, start_img, 0.25)  # Adjust coordinates
        self.end_button = Button(860, 560, exit_img, 0.25)  # Adjust coordinates
        self.backmenu_button = Button(860, 680, backmenu_img, 0.25)

    def clear_buttons(self):
        self.start_button = None
        self.end_button = None
        self.backmenu_button = None

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))

        # X as Width and Y as Height for the Game Over Text Dimension
        x_position = 840
        y_position = 450
        text_rect = text.get_rect(
            topleft=(x_position, y_position)
        )  # define the dimension
        self.screen.blit(text, text_rect)

        # Draw buttons and handle events
        in_game_over_screen = True

        while in_game_over_screen:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
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

        # Add a break statement to exit the loop completely
        self.clear_buttons()

    def restart_game(self):
        self.game_instance.game_over = False  # Reset game state
        self.game_instance.score = 0  # Reset score
        self.game_instance.pipes.empty()  # Clear pipes
        self.game_instance.bird.rect.y = self.screen_height // 2  # Reset bird position
        self.game_instance.run()

    def return_menu(self):
        from main_menu import Menu

        main_menu = Menu(self.screen, screen_height=1080, screen_width=1920)
        main_menu.reset_button_states()  # Added to reset button states
        main_menu.run()

        if main_menu.menu_state == "main_menu":
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    # Use Bird1 as the default character
    selected_character = Bird1
    game = Game(1920, 1080, selected_character=selected_character)
    game.run()
    pygame.quit()
