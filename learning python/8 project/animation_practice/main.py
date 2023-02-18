import random
import time

import pygame
import pymunk.pygame_util

WIDTH = 700
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
X = 100
Y = 600
speed = 10
models = []
clock_ = pygame.time.Clock()
FPS = 60
W_RECT = 60
H_RECT = 4
animation_count = 0

pymunk.pygame_util.positive_y_is_up = False
# переменные Pymunk

draw_options = pymunk.pygame_util.DrawOptions(screen)
for i in range(1, 10):
    models.append(pygame.image.load(f'images/image_part_00{i}.png'))
models.append(pygame.image.load(f'images/image_part_0010.png'))
ball_x = 20
ball_y = 20

while running:
    get_pressed = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    ball_y += 5

    if X <= -70:
        X = 700
    elif X >= 700:
        X = -70
    if get_pressed[pygame.K_RIGHT]:
        X += speed
    elif get_pressed[pygame.K_LEFT]:
        X -= speed

    pygame.draw.rect(screen, "White", (X, Y, W_RECT, H_RECT))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock_.tick(FPS)
pygame.quit()
