import pygame

pygame.init()
W = 900
H = 1200
screen = pygame.display.set_mode((H,W))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

