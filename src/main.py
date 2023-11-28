import pygame
import bird
#constant
WIDTH = 1920
HEIGHT = 1080

class Main:
   
   #intialize game 
   pygame.init()
   #define the resolution
   screen = pygame.display.set_mode((WIDTH,HEIGHT))
   #Title
   pygame.display.set_caption("Flappy Bird Clone")
   #Icon
     
   
   #create sprite group for bird + pipe
   birds = pygame.sprite.Group()   
   #creat bird object + add to sprite groups
   initialX = WIDTH / 8
   initialY = HEIGHT / 2
   bird1 = bird.FlappyBird(initialX,initialY)
   birds.add(bird1)

   
   #Game Loop
   gameOn = True
   
   while gameOn:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameOn = False
            
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               bird1.flap()               
               
         if event.type == pygame.KEYUP:
            pass
      
      screen.fill((0,0,0))
      bird1.update(HEIGHT)
      screen.blit(bird1.img, bird1.rect)#(bird1.x, bird1.y))
      #update display
      pygame.display.update()

   
   