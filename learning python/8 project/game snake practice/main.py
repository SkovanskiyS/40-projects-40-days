import os, pygame, time
import random
from os import listdir

WIDTH = 600
HEIGH = 600
FPS = 60
run = True
player_speed = 5
player_x, player_y = 100, 100
coin_x, coin_y = 300, 150
is_Jumped = False
pixels_to_jump = 7

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

    keys = pygame.key.get_pressed()
    screen.blit(pygame.transform.scale(coin_img, (40, 40)), (coin_x, coin_y))
    screen.blit(bg, (0, 0))
    elapsed = 0
    elapsed = pygame.time.get_ticks() - elapsed

    if keys[pygame.K_UP] or keys[pygame.K_w] and player_y > 5:
        player_y -= player_speed
        print('вверх')
        screen.blit(pygame.transform.scale(walks[1], (67, 120)), (player_x, player_y))
    elif keys[pygame.K_DOWN] or keys[pygame.K_s] and player_y <= 450:
        player_y += player_speed
        print('вниз')
        screen.blit(pygame.transform.scale(walks[2], (67, 120)), (player_x, player_y))
    elif keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 5:
        player_x -= player_speed
        print('влево')
        screen.blit(pygame.transform.scale(walks[3], (67, 120)), (player_x, player_y))
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x <= 530:
        player_x += player_speed
        print('направо')
        screen.blit(pygame.transform.scale(walks[4], (67, 120)), (player_x, player_y))
    else:
        if elapsed > 500:
            screen.blit(pygame.transform.scale(walks[0], (67, 120)), (player_x, player_y))
    # if keys[pygame.K_RIGHT] and pygame[pygame.K_DOWN]:
    #     player_x += player_speed
    #     player_y += player_speed
    #     print('ДЫА')
    #     screen.blit(pygame.transform.scale(walks[4], (67, 120)), (player_x, player_y))
    # jump physic
    if not is_Jumped:
        if keys[pygame.K_SPACE]:
            is_Jumped = True
    else:
        if pixels_to_jump >= -7:
            if pixels_to_jump > 0:
                player_y -= (pixels_to_jump ** 2) / 2
            else:
                player_y += (pixels_to_jump ** 2) / 2
            pixels_to_jump -= 1
        else:
            is_Jumped = False
            pixels_to_jump = 7

        # player_y += pixels_to_jump
        # screen.blit(pygame.transform.scale(walks[0], (67, 120)), (player_y, player_x))

    print(coin_x)
    print(player_x)
   # check for coin
    if coin_x - 15 <= player_x <= coin_x + 15 and coin_y - 50 <= player_y <= coin_y + 50:
        print('да')

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
