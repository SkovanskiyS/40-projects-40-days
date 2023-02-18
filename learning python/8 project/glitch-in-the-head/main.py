import pygame
from Rocket import Rocket

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#white side
left_side = pygame.Surface((WIDTH//2,HEIGHT))
left_side.fill('White')
screen.blit(left_side,(0,0))
pygame.display.update()

rocket_x = 0
rocket_y = 0

def main():
    running = True

    rocket = Rocket(left_side,rocket_x,rocket_y,10)
    screen.blit(rocket.draw(screen,"Black"),(30,30))
    rocket.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    pygame.display.update()


if __name__ == '__main__':
    main()
