import pygame, time
pygame.init()
screen=pygame.display.set_mode((600,600))

pygame.display.set_caption("Birthday Cards")
fontstyle = pygame.font.SysFont("times new roman", 50)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    image1 = pygame.image.load("birthdayimage1.jpg")
    screen.blit(image1,(0,0))
    text = fontstyle.render("Happy birthday to you.", True, "black")
    screen.blit(text, (45,45))
    pygame.display.update()
    time.sleep(2)
      
    image2 = pygame.image.load("birthdayimage2.jpg")
    screen.blit(image2,(0,0))
    text2 = fontstyle.render("have a blessed day.", True, "black")
    screen.blit(text2, (45,45))
    pygame.display.update()
    time.sleep(2)

    image3 = pygame.image.load("birthdayimage3.jpg")
    screen.blit(image3,(0,0))
    text3 = fontstyle.render("hope you had a good day.", True, "black")
    screen.blit(text3, (45,10))
    pygame.display.update()
    time.sleep(2)