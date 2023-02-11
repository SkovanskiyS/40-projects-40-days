import time

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
player_x = 100
playex_y = 100

models = []
clock_ = pygame.time.Clock()

animation_count = 0

for i in range(1, 10):
    models.append(pygame.image.load(f'images/image_part_00{i}.png'))
models.append(pygame.image.load(f'images/image_part_0010.png'))

while running:
    clock_.tick(30)
    screen.fill((255, 255, 255))
    screen.blit(models[animation_count], (100, 100))
    if animation_count == 9:
        animation_count = 0
    else:
        animation_count += 1
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
pygame.quit()
