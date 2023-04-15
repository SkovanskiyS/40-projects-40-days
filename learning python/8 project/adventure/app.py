import pygame

pygame.init()
W = 900
H = 600
FPS = 60
SCORE = 0
screen = pygame.display.set_mode((W, H))
running = True
pygame.display.set_caption('Adventure Game')
clock = pygame.time.Clock()

# image surface
statue_surface = pygame.image.load(r'objects/statue.png').convert_alpha()
transformed_surface = pygame.transform.scale(statue_surface, (80, 127))
statue_rect = transformed_surface.get_rect(topleft=(100, 300))

# text
font_text = pygame.font.Font(None, 50)
text_surface = font_text.render('Your score: ', True, 'Red')
text_rect = text_surface.get_rect(topleft=(350, 10))

# player
player_sprite = [pygame.image.load(fr'objects/player/stay{sprite}.png').convert_alpha() for sprite in range(1, 8)]
j = 0
player_rect = pygame.transform.scale(player_sprite[0], (70, 70)).get_rect(topleft=(250, 100))
player_gravity = 10
jumped = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if j >= 7: j = 0
    p_surface = pygame.transform.scale(player_sprite[j], (70, 70))
    pressed = pygame.key.get_pressed()

    # controller
    if pressed[pygame.K_d] and player_rect.right <= 850:
        player_rect.left += 5
    elif pressed[pygame.K_a] and player_rect.left >= -22:
        player_rect.right -= 5
    elif pressed[pygame.K_s] and player_rect.bottom <= 550:
        player_rect.top += 5
    elif pressed[pygame.K_w] and player_rect.top >= -25:
        player_rect.bottom -= 5

    # background
    screen.blit(pygame.image.load(r'objects/bg/bg.png').convert(), (0, 0))
    # show up

    screen.blit(text_surface, text_rect)
    screen.blit(font_text.render(str(SCORE), True, 'Red'), (550, 10))
    screen.blit(transformed_surface, statue_rect)

    if not jumped:
        if pressed[pygame.K_SPACE]:
            jumped = True
    else:
        if player_gravity >= -10:
            if player_gravity > 0:
                player_rect.y -= (player_gravity ** 2) / 4
            else:
                player_rect.y += (player_gravity ** 2) / 4
            player_gravity -= 1
        else:
            jumped = False
            player_gravity = 10

    screen.blit(p_surface, player_rect)

    # # ---- DRAWING ------
    # # player rect
    # pygame.draw.rect(screen, 'white', player_rect, 1)
    #
    # # statue draw
    # pygame.draw.rect(screen, 'white', statue_rect, 1)
    #
    # # player line draw
    # pygame.draw.aaline(screen, 'Red', player_rect.center, pygame.mouse.get_pos(), 10)
    #
    # # text draw
    # pygame.draw.rect(screen, 'white', text_rect, 1)

    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption("Fps: " + str(round(clock.get_fps())))
    j += 1

pygame.quit()
