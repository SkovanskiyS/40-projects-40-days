import time

import pygame, os
import random

# variables
WIDTH = 1400
HEIGHT = 700
running = True
FPS = 30
# init pygame
pygame.init()


# set screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#uploading images
walking, w_length = [], 0
standing, s_length = [], 0
fighting, f_length = [], 0
dying, d_length = [], 0
all_elem_dir = os.listdir()
for item in all_elem_dir:
    if item.startswith('w'):
        path = os.getcwd() + '/walking/'
        path_list = os.listdir(os.getcwd() + '/walking/')
        print(path_list)
        for item2 in path_list:
            w_length += 1
            walking.append(pygame.image.load(path + f'/{item2}'))
    elif item.startswith('s'):
        path = os.getcwd() + '/standing/'
        path_list = os.listdir(os.getcwd() + '/standing/')
        for item2 in path_list:
            s_length += 1
            standing.append(pygame.image.load(path + f'/{item2}'))
    elif item.startswith('f'):
        path = os.getcwd() + '/fighting/'
        path_list = os.listdir(os.getcwd() + '/fighting/')
        for item2 in path_list:
            f_length += 1
            fighting.append(pygame.image.load(path + f'/{item2}'))
    elif item.startswith('d'):
        path = os.getcwd() + '/dying/'
        path_list = os.listdir(os.getcwd() + '/dying/')
        for item2 in path_list:
            d_length += 1
            dying.append(pygame.image.load(path + f'/{item2}'))

i = 0
clock = pygame.time.Clock()

while running:
    screen.fill((173, 216, 230))
    screen.blit(walking[i], (WIDTH / 2, HEIGHT / 2))
    print(i)
    print(w_length)
    if i >= w_length-1:
        i = 0
    else:
        i += 1
    pygame.display.update()

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
