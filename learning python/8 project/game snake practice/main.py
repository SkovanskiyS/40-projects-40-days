import os
import time

import pygame
from os import listdir

WIDTH = 600
HEIGH = 600
FPS = 30
run = True

# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()
# background
bg = pygame.image.load('image/Garden-Background.png')
icon = pygame.image.load('image/icon.png')

# set bg and icon
pygame.display.update()
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake by Kovanskiy')

walks = []
path_of_walk = os.getcwd()+'/image/moves'
for dir2 in listdir(path_of_walk):
    walks.append(pygame.image.load(path_of_walk+"/"+dir2))

i = 0

while run:
    screen.blit(bg, (0, 0))
    screen.blit(pygame.transform.scale(walks[i], (67, 120)), (100, 100))
    if i>3:i=0
    else: i+=1
    pygame.display.update()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
pygame.quit()
