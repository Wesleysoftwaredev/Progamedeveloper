import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))

pygame.display.set_caption("Ball Bouncer")
b1 = pygame.draw.circle(surface = screen, color = "black", center = [25,25], radius = 60)
speed = [1,1]
screen.fill("green")
while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
             exit()
        screen.fill("green")
        b1 = b1.move(speed)
        if b1.left<0 or b1.right>1000:
            speed[0]=-speed[0]
        if b1.top<0 or b1.bottom>500:
            speed[1]=-speed[1]
        pygame.draw.circle(surface = screen, color = "black", center = b1.center, radius = 60)
        pygame.display.update()