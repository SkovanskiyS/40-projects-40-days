import os, pygame, time
import random
from os import listdir

WIDTH = 600
HEIGH = 600
FPS = 60
run = True
player_speed = 5
player_x = 100
player_y = 100
coin_x = 300
coin_y = 150

# init
pygame.init()
pygame.mixer.init()
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
path_of_walk = os.getcwd() + '/image/moves'
for dir2 in listdir(path_of_walk):
    walks.append(pygame.image.load(path_of_walk + "/" + dir2))

# set music
bg_sound = pygame.mixer.Sound('audio/music.wav')
bg_sound.play()
bg_sound.set_volume(0.1)


def random_coin():
    # load_img
    pass


coin_img = pygame.image.load('image/coin.png')

pygame.display.update()

while run:
    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()
    screen.blit(pygame.transform.scale(coin_img, (40, 40)), (coin_x, coin_y))
    if keys[pygame.K_UP]:
        player_x -= player_speed
        print('вверх')
        screen.blit(pygame.transform.scale(walks[1], (67, 120)), (player_y, player_x))
    elif keys[pygame.K_DOWN]:
        player_x += player_speed
        print('вниз')
        screen.blit(pygame.transform.scale(walks[2], (67, 120)), (player_y, player_x))
    elif keys[pygame.K_LEFT]:
        player_y -= player_speed
        print('влево')
        screen.blit(pygame.transform.scale(walks[3], (67, 120)), (player_y, player_x))
    elif keys[pygame.K_RIGHT]:
        player_y += player_speed
        print('направо')
        screen.blit(pygame.transform.scale(walks[4], (67, 120)), (player_y, player_x))
    else:
        screen.blit(pygame.transform.scale(walks[0], (67, 120)), (player_y, player_x))

    # check for coin
    if coin_x == player_x or coin_y == player_y:
        coin_x += random.randint(30, 400)
        coin_y += random.randint(30, 400)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
