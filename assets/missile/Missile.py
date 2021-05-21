import pygame
import math


class Missile(pygame.sprite.Sprite):
    def __init__(self, screen, screensize, x, speed):
        super().__init__()
        self.time = pygame.time.get_ticks()
        self.moving = False
        self.scale = 0.005
        img = pygame.image.load("assets/missile/missile00.png").convert_alpha()
        self.image = pygame.transform.scale(img, (int(self.scale * img.get_width() * screensize[1]),
                                                  int(self.scale * img.get_height() * screensize[1])))
        self.speed = speed
        self.x = x
        self.y = 0
        self.lastDraw = 0
        self.screen = screen
        self.screensize = screensize
        self.rect = self.image.get_rect()

    def draw(self, dt):
        time = pygame.time.get_ticks() - self.time
        self.y = int(dt * math.pow(time / 100, 3) * self.screensize[1] / 10000)
        self.screen.blit(self.image, (int(self.x - self.rect[2] / 2), int(self.y - self.rect[3] / 2)))
        return self.y > self.screensize[1]

    def collide(self, other):
        return (self.rect[0] + self.x < other.rect[0] + other.x < self.rect[2] + self.x
                or self.rect[0] + self.x < other.rect[2] + other.x < self.rect[2] + self.x) \
               and (self.rect[1] + self.y < other.rect[1] + other.y < self.rect[3] + self.y
                    or self.rect[1] + self.y < other.rect[3] + other.y < self.rect[3] + self.y)
