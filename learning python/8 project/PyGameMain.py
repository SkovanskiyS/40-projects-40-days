import pygame

pygame.init()
W = 512
H = 512
screen = pygame.display.set_mode((W,H))
run = True

rect1 = pygame.Rect((10, 10, 10, 10))
print(rect1.size)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
