import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))

class r1:
    def __init__(self, color, dimensions):
        self.screen=screen
        self.color=color
        self.dimensions=dimensions
    def draw(self):
        self.drawrect=pygame.draw.rect(self.screen, self.color, self.dimensions)
yellowr = r1("yellow", (70,70,100,100))
greenr = r1("green", (30,30,200,200))
redr = r1("red", (5,5,250,100))
purpler = r1("purple", (50,50,100,100))
pinkr = r1("pink", (90,90,100,190))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("white")
    yellowr.draw()
    greenr.draw()
    redr.draw()
    purpler.draw()
    pinkr.draw()
    pygame.display.update()