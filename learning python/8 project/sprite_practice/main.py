# import pygame
# from pygame.color import THECOLORS
#
# #initialize
# pygame.init()
# W = 600
# H = 600
# FPS = 60
# screen = pygame.display.set_mode((W, H))
# pygame.display.set_caption('hi')
# clock = pygame.time.Clock()
# screen.fill(THECOLORS['antiquewhite4'])
# pygame.display.update()
#
# # sprites
# background_image = pygame.image.load("Tile_25-512x512.png")
# run = True
#
# # load image
#
# while run:
#     for event in pygame.event.get():
#         pressed_key = pygame.key.get_pressed()
#         if event.type == pygame.QUIT or pressed_key[pygame.K_ESCAPE]:
#             run = False
#     pygame.display.update()
#
#     clock.tick(FPS)
#
# pygame.quit()

import pygame

screen = pygame.display.set_mode((500,500))
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.display.update()

pygame.quit()