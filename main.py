import pygame 

pygame.init()

screen = pygame.display.set_mode([500,500])

RED = (255,0,0)
GREEN = (0,255,0)
BLUE =(0,0,255)
YELLOW = (255,255,0)
WHITE =(255,255,255)
BLACK =(0,0,0)

position = (300,300)
radius = 50 
wid = 20

screen.fill(WHITE)
pygame.draw.circle(screen, RED, position,radius, wid)

class Circle():
    def __init__ (self,colour,pos,radius,width=0):
        self.screen = screen
        self.colour =colour
        self.pos = pos
        self.radius =radius
        self.width = width 

    def drawCircle(self):
        pygame.draw.circle(self.screen,self.colour, self.pos, self.radius, self.width)

    def grow(self,r):
        self.radius = self.radius+r
        pygame.draw.circle(self.screen,self.colour,self.pos, self.radius, self.width)
    
p1 = Circle(BLUE,position,radius+90,4)
p2 = Circle(GREEN,position,radius+60,1)
p3 = Circle(YELLOW,position,radius+45,6)
p4 = Circle(RED,position,radius+30,3)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            p1.drawCircle()
            p2.drawCircle()
            p3.drawCircle()
            p4.drawCircle()
        if(event.type == pygame.MOUSEBUTTONUP):
            p1.grow(1)
            p2.grow(2)
            p3.grow(3)
            p4.grow(4)
        if(event.type == pygame.MOUSEMOTION):
            pos1= pygame.mouse.get_pos()
            p5= Circle(BLACK,pos1,5)
            p5.drawCircle()
            
    pygame.display.update()