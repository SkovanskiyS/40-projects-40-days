import pygame, Rocket

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#white side
left_side = pygame.Surface((WIDTH//2,HEIGHT))
left_side.fill('White')
screen.blit(left_side,(0,0))
pygame.display.update()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()



if __name__ == '__main__':
    main()
