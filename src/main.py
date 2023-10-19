#this is where we call all class, mostly deaslling with ui and stuff
# delete this line later. We mostly  put some for loop function here to call several classes many times

# Create a Main class
import pygame
class Main:
   def __init__(self):
      #Game HUD, UI, interactive buttons and stuf
      pass
   
   #intialize game 
   pygame.init()
   
   #define the resolution
   screen = pygame.display.set_mode((1280,720))
   
   #Title
   pygame.display.set_caption("Flappy Bird Clone")
   #Icon
   
   #Game Loop
   gameOn = True
   
   while gameOn:
      for event in pygame.event.get():
         if event.type() == pygame.QUIT:
            gameOn = False
      #update display
      pygame.display.update()

   
   