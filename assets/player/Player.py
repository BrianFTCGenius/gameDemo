import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, screensize, *, controls: list = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]):
        super().__init__()
        self.frame = 0
        self.moving = False
        self.img = []
        self.scale = 0.0005
        self.x = screensize[0] * 0.75
        self.y = screensize[1] * 0.75
        self.lastDraw = 0
        self.facingRight = True
        self.screen = screen
        self.screensize = screensize
        self.controls = controls
        for i in range(7):
            img = pygame.image.load(f"assets/player/idle/robot-idle-{i + 1}.png").convert_alpha()
            self.img.append(pygame.transform.scale(img, (int(self.scale * img.get_width() * screensize[1]),
                                                         int(self.scale * img.get_height() * screensize[1]))))
        for i in range(7):
            img = pygame.image.load(f"assets/player/run/robot-run-{i + 1}.png").convert_alpha()
            self.img.append(pygame.transform.scale(img, (int(self.scale * img.get_width() * screensize[1]),
                                                         int(self.scale * img.get_height() * screensize[1]))))
        self.rect = self.img[0].get_rect()

    def handle_keys(self, dt, speed):
        dist = speed * self.screensize[1] * dt  # distance moved in 1 frame, try changing it to 5
        key = pygame.key.get_pressed()
        self.moving = False
        # if key[self.controls[0]]:  # up key
        #     self.y -= int(dist)  # move up
        #     self.moving = True

        if key[self.controls[1]]:  # left key
            self.x -= int(dist)  # move left
            self.moving = True
            self.facingRight = False

        # if key[self.controls[2]]:  # down key
        #     self.y += int(dist)  # move down
        #     self.moving = True

        if key[self.controls[3]]:  # right key
            self.x += int(dist)  # move right
            self.moving = True
            self.facingRight = True

    def draw(self):
        self.animate()
        if self.x < 0:
            self.x = self.screensize[0]
        elif self.x > self.screensize[0]:
            self.x = 0
        if self.y < 0:
            self.y = 0
        elif self.y > self.screensize[1]:
            self.y = self.screensize[1]
        if self.moving:
            offset = 7
        else:
            offset = 0
        if self.facingRight:
            img = self.img[self.frame + offset]
        else:
            img = pygame.transform.flip(self.img[self.frame + offset], True, False)
        self.screen.blit(img,
                         (int(self.x + self.rect[2] / 2 - img.get_width()),
                          int(self.y + self.rect[3] / 2 - img.get_height())))

    def animate(self):
        ct = pygame.time.get_ticks()
        if ct - self.lastDraw > 40:                # animation loop
            self.frame += 1
            self.lastDraw = ct
        if self.frame == 7:
            self.frame = 0

    def collide(self, other):
        return (self.rect[0] + self.x < other.rect[0] + other.x < self.rect[2] + self.x
                or self.rect[0] + self.x < other.rect[2] + other.x < self.rect[2] + self.x) \
               and (self.rect[1] + self.y < other.rect[1] + other.y < self.rect[3] + self.y
                    or self.rect[1] + self.y < other.rect[3] + other.y < self.rect[3] + self.y)
