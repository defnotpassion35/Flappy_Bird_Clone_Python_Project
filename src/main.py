import pygame
import sys
import random
from bird import FlappyBird 
from pipe import Pipe

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width  = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Set up colors
white = (255, 255, 255)
GRAY = (128, 128, 128)


# Set up clock
clock = pygame.time.Clock()

# Create sprite groups
birds = pygame.sprite.Group()
pipes = pygame.sprite.Group()

# Set up the bird
bird = FlappyBird(screen_width // 4, screen_height // 2)  # Initial position
birds.add(bird)

# Set up pipes
pipe_gap = 300
pipe_spawn_frequency = 60  # in frames
pipe_spawn_timer = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update bird
    bird.update(screen_height)
    
    # Update the pipes
    speed = 5  # Set a constant speed
    pipes.update(speed)  
     
    # Spawn pipes
    pipe_spawn_timer += 1
    if pipe_spawn_timer == pipe_spawn_frequency:
        pipe_height = random.randint(200, 600)
        new_pipe = Pipe(screen_width, pipe_height, pipe_gap)
        pipes.add(new_pipe)
        pipe_spawn_timer = 0


    # Remove offscreen pipes
    for pipe in pipes:
        if pipe.offscreen():
            pipes.remove(pipe)

    # Check for collisions with pipes
    for pipe in pipes:
        if bird.rect.x < pipe.x + pipe.width and bird.rect.x + bird.rect.width > pipe.x:
            if bird.rect.y < pipe.height or bird.rect.y + bird.rect.height > pipe.height + pipe.gap:
                print("Ouch! You hit a pipe!")
                pygame.quit()
                sys.exit() 

    # Draw everything
    screen.fill(white)

    # Draw pipes first
    for pipe in pipes:
        pipe.draw(screen, GRAY)  # Pass the pipe color

    # Draw bird last
    bird.draw(screen)

    pygame.display.flip()


    # Cap the frame rate
    clock.tick(60)  # Adjust as needed
