import time

import pygame

pygame.init()
W = 900
H = 600
FPS = 60
score = 0
screen = pygame.display.set_mode((W, H))
running = True
pygame.display.set_caption('Adventure Game')
clock = pygame.time.Clock()

# image surface
first_surface = pygame.image.load(r'objects/statue.png')
transformed = pygame.transform.scale(first_surface, (80, 127))

# text
font_text = pygame.font.Font(None, 50)
text_surface = font_text.render('Your score: ', True, 'Red')

# player
player_sprite = [pygame.image.load(fr'objects/player/stay{sprite}.png') for sprite in range(1, 8)]
j = 0
player_x_pos = 0
player_y_pos = 0
while running:
    screen.fill((0, 255, 255))
    pressed = pygame.key.get_pressed()
    if j >= 7: j = 0

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif pressed[pygame.K_w]:
            score += 1
        elif pressed[pygame.K_s]:
            score -= 1

    # show up
    screen.blit(transformed, (200, 100))
    screen.blit(text_surface, (350, 10))
    screen.blit(font_text.render(str(score), True, 'Red'), (550, 10))

    # controller
    if pressed[pygame.K_d] and player_x_pos <= 830:
        player_x_pos += 5
    elif pressed[pygame.K_a] and player_x_pos >= -22:
        player_x_pos -= 5
    elif pressed[pygame.K_s] and player_y_pos <= 500:
        player_y_pos += 5
    elif pressed[pygame.K_w] and player_y_pos >= -35:
        player_y_pos -= 5

    screen.blit(pygame.transform.scale(player_sprite[j], (100, 100)), (player_x_pos, player_y_pos))

    pygame.display.update()
    clock.tick(FPS)
    j += 1

pygame.quit()
