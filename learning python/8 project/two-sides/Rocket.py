import pygame


class Rocket:
    width = 10
    height = 30

    def __init__(self, surface, x, y, speed):
        self.surf = surface
        self.r_x = x
        self.r_y = y
        self.speed = speed

    def update(self):
        self.r_y -= self.speed
        if self.r_y < 0:
            self.r_y = 300

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.r_x, self.r_y, self.width, self.height))
