#code bird class, include many attributes and methods
#--------------------Attributes or properties----------------------------------
#possible function attributes: x_position, top and bottom pipe,
# possible instace attribute: heigth, width 

#-----------------Methods-----------------------
#Possible methods: draw(), update()
# Create a Pipe class
class Pipe:
    #define constant 
    PIPE_WIDTH = 80
    PIPE_GAP = 200
    PIPE_X = WIDTH
    PIPE_SPEED = 2
    
    def __init__(self,x,y,):
        # Initialize attributes for the pipe
        pass

    def move(self):
        # Implement the pipe's movement
        pass
    def draw(self):
        pass
    
#Testing genvironment
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

