import time

import pygame, os
import random

import screeninfo
import win32api

# variables
WIDTH = win32api.GetSystemMetrics(0)
HEIGHT = win32api.GetSystemMetrics(1)
running = True
FPS = 30
# init pygame
pygame.init()
player_x = 300
player_y = 700

# set screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# uploading images
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
    # screen.blit(pygame.image.load(
    #     r"C:\Users\jahon\Documents\GitHub\40-projects-40-days\learning python\8 project\game snake practice\image\background.jpg"),
    #     (0, 0))
    pressed_key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    elapsed = 0
    if pressed_key[pygame.K_RIGHT]:
        player_x += 30
        screen.blit(walking[i], (player_x, player_y))
    elif pressed_key[pygame.K_LEFT]:
        player_x -= 30
        screen.blit(pygame.transform.flip(walking[i],True,False),(player_x,player_y))
    else:
        elapsed = pygame.time.get_ticks() - elapsed
        if elapsed>10000:
            screen.blit(standing[i], (player_x, player_y))
    if i >= s_length - 1:
        i = 0
    else:
        i += 1
    pygame.display.update()

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_key[pygame.K_ESCAPE]:
            running = False

pygame.quit()
