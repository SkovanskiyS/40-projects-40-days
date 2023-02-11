import pygame

pygame.init()
screen_size = pygame.display.set_mode((512,512))
pygame.display.set_caption('Learning Pygame')
run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()



