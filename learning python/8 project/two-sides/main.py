import pygame
from Rocket import Rocket

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# white side
left_side = pygame.Surface((WIDTH // 2, HEIGHT))
left_side.fill('White')

right_side = pygame.Surface((WIDTH // 2, HEIGHT))
right_side.fill("Black")

rocket_x = left_side.get_width() // 2
rocket_y = left_side.get_height() // 2


def main():
    running, left_active, right_active = True, False, False
    rocket_left = Rocket(left_side, rocket_x, rocket_y, 10)
    rocket_right = Rocket(right_side, right_side.get_width() * 1.5, rocket_y, 10)
    while running:
        screen.blit(right_side, (left_side.get_width(), 0))
        screen.blit(left_side, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > 250:
                    right_active = True
                    left_active = False
                else:
                    left_active = True
                    right_active = False
        if right_active:
            rocket_right.draw(screen, "White")
            rocket_right.update()
        elif left_active:
            rocket_left.draw(screen, "Black")
            rocket_left.update()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
