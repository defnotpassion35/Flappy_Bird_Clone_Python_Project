import pygame
import sys
import random
from bird import FlappyBird 
from pipe import Pipe
from game_over import GameOver

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()

        # Set up the screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Flappy Bird")

        # Set up colors
        self.white = (255, 255, 255)
        self.GRAY = (128, 128, 128)

        # Set up clock
        self.clock = pygame.time.Clock()

        # Create sprite groups
        self.birds = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        
        # Set up Score
        self.score = 0
        self.font = pygame.font.Font(None, 36)

        # Set up the bird
        self.bird = FlappyBird(screen_width // 4, screen_height // 2, "plane.png")  # Initial position
        self.birds.add(self.bird)

        # Set up pipes
        self.pipe_gap = 300
        self.pipe_spawn_frequency = 80  # in frames
        self.pipe_spawn_timer = 0

        # Set up game_over screen
        self.game_over = False
        self.game_over_screen = GameOver(self.screen, self.screen_width, self.screen_height)

    def run(self):
        # Game loop
        while not self.game_over:
            for event in pygame.event.get():
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
            # Increase score
            for pipe in self.pipes :
                if self.bird.x == pipe.x  + 80:  #and not game_over:
                    self.score += 1
                    print(self.score) 

            # Draw everything
            self.screen.fill(self.white)

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
            
        self.game_over_screen.game_over_screen()

if __name__ == "__main__":
    game = Game(1920, 1080)
    game.run()
