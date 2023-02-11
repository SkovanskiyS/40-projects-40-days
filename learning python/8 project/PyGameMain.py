import pygame

pygame.init()
W = 512
H = 512
screen = pygame.display.set_mode((W, H))
img = pygame.image.load('img/randomPic2.png')
pygame.display.set_icon(img)
pygame.display.set_caption('Glitc-in-the-Head')  # GITH
run = True
square = pygame.Surface((50, 50))

# square.fill('Blue')
# screen.blit(square, (W / 2-25, H / 2-25))
# pygame.display.update()

text_fonts = pygame.font.Font("fonts/Roboto-Bold.ttf",40)
text_surface = text_fonts.render("Hello, World",True,'White','Green')

while run:
    screen.blit(pygame.transform.scale(img, (3, 210)),(100,20))
    #screen.blit(text_surface,(30,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


pygame.quit()


