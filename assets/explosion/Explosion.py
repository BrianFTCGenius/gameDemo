import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, screen, screensize, x: int, y: int, scale: float = 0.001):
        super().__init__()
        self.frame = 0
        self.img = []
        self.scale = scale
        self.x = x
        self.y = y
        self.lastDraw = 0
        self.screen = screen
        self.screensize = screensize
        for i in range(7):
            img = pygame.image.load(f"explosion_6-{i + 1}.png").convert_alpha()
            self.img.append(pygame.transform.scale(img, (int(self.scale * img.get_width() * screensize[1]),
                                                         int(self.scale * img.get_height() * screensize[1]))))

    def draw(self):
        self.animate()
        self.screen.blit(self.img[self.frame],
                         (int(self.x + self.rect[2] / 2 - self.img[self.frame].get_width()),
                          int(self.y + self.rect[3] / 2 - self.img[self.frame].get_height())))

    def animate(self):
        ct = pygame.time.get_ticks()
        if ct - self.lastDraw > 100:  # animation loop
            self.frame += 1
            self.lastDraw = ct
        if self.frame == 7:
            self.frame = 0
