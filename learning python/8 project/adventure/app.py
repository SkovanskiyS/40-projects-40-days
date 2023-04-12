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


while running:
    score_text = font_text.render(str(score), True, 'Red')
    screen.fill((0, 255, 255))
    pressed = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif pressed[pygame.K_SPACE]:
            score += 1
    screen.blit(transformed, (200, 100))
    screen.blit(text_surface, (350, 10))
    screen.blit(score_text, (550, 10))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
