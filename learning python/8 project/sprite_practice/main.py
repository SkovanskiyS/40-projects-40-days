import pygame

pygame.init()
W = 1024
H = 900
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('hi')

# sprites

background_image = pygame.image.load("Tile_25-512x512.png")
bg = pygame.transform.scale(background_image,(screen.get_width(),screen.get_height()))
run = True


#load image
first = pygame.image.load('player/1.png')
sec = pygame.image.load('player/2.png')
th = pygame.image.load('player/3.png')
f = pygame.image.load('player/4.png')
fivth = pygame.image.load('player/5.png')
six = pygame.image.load('player/6.png')

while run:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        pressed_key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or pressed_key[pygame.K_ESCAPE]:
            run = False
    pygame.display.update()

pygame.quit()






