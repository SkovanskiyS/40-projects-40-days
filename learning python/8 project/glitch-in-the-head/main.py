import pygame

WIDTH = 800
HEIGHT = 800
FPS = 60
a = 0


class Rocket:
    w = 20
    h = 50

    def __int__(self, surface, color):
        self.surf = surface
        self.color = color

        self.x = surface.get_width() // 2 - Rocket.w
        self.y = surface.get_height() // 2 - Rocket.h

    def fly(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.w, Rocket.h))
        self.y -= 3

        if self.y < -Rocket.h:
            self.y = HEIGHT


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    surf_left = pygame.Surface((WIDTH // 2, HEIGHT))
    surf_left.fill("White")
    surf_right = pygame.Surface((WIDTH // 2, HEIGHT))
    screen.blit(surf_left, (0, 0))
    screen.blit(surf_right, (WIDTH // 2, 0))
    rocket_left = Rocket(surf_left,"Black")
    rocket_right = Rocket(surf_right,"White")
    active_left = False
    active_right = False
    while run:

        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < WIDTH // 2:
                    # то активируем левую,
                    # отключаем правую
                    active_left = True
                    active_right = False
                elif event.pos[0] > WIDTH // 2:
                    # иначе - наоборот
                    active_right = True
                    active_left = False

        if active_left:
            # Если активна левая поверхность,
            # то заливаем только ее цветом,
            surf_left.fill("WHITE")
            # поднимаем ракету,
            rocket_left.fly()
            # заново отрисовываем левую
            # поверхность на главной.
            screen.blit(surf_left, (0, 0))
        elif active_right:
            surf_right.fill("BLACK")
            rocket_right.fly()
            screen.blit(surf_right, (WIDTH // 2, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
