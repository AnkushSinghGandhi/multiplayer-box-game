# importing few things
import pygame
from network import Network

# width and height for game window
width = 500
height = 500
# seting up window
win = pygame.display.set_mode((width,height))
# seting window title to be "client"
pygame.display.set_caption("client")

# variable that stores clients no.
clientnumber = 0

# player class
class Player():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 1
    
    # function to create a box on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    # function to set movement of box
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val
            
        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

        # changing box's x,y axis a box again
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str(1))

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# function to draw box on screen and update the screen
def redrawwindow(win,player):
    # filling the screen with white color
    win.fill((255,255,255))
    # drawing an box on window
    player.draw(win)
    # updating the display
    pygame.display.update()

# main function
def main():
    # setting run variable True
    run = True
    # creating a Network class object
    n = Network()
    startpos = read_pos(n.getpos())
    # creating 1st player
    p1 = Player(startpos[0],startpos[1],100,100,(0,255,0))
    # creating 2nd player
    p2 = Player(0,0,100,100,(0,255,0))

    # game loop
    while run:
        # checking for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # setting the run variable False
                run = False
                pygame.quit()
        # calling move methode from player class
        p.move()
        # redrawing box and updating screen
        redrawwindow(win,p)

# calling the main function
main()