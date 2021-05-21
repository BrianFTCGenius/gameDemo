import pygame
import math
from random import randint
from assets.player.Player import Player
from assets.missile.Missile import Missile
pygame.init()
size = pygame.display.list_modes()[0]
screen = pygame.display.set_mode(size, pygame.WINDOWMAXIMIZED)
pygame.display.set_caption("Helicopter Escape")
screensize = pygame.display.get_surface().get_size()


def main():
    clock = pygame.time.Clock()
    running = True
    pygame.mixer.init()
    # pygame.mixer.Channel(0).play(pygame.mixer.Sound('Assets\helicopters\helicopter.wav'))
    # pygame.mixer.music.load("Assets/main.mp3")
    # pygame.mixer.music.play(-1)
    missile = []
    player = Player(screen, screensize)
    font = pygame.font.SysFont(None, int(screensize[0] / 10))
    img = font.render('Score: 0', True, (255, 0, 0))
    lastTime = pygame.time.get_ticks()
    level = 1
    score = 0
    spawnList = []
    while running:
        if pygame.time.get_ticks() - lastTime > 2000:
            level += 1
            lastTime = pygame.time.get_ticks()

        if len(missile) < level:
            possible = True
            x = randint(0, screensize[0])
            for i in missile:
                if x - screensize[0] / 100 < i.x < x - screensize[0] / 100:
                    possible = False
            if possible:
                missile.append(Missile(screen, screensize, x, level))
                spawnList.append(x)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        dt = int(clock.tick(60) / 50 + 1)

        pygame.display.update((0, 0, screensize[0], screensize[1]))
        player.handle_keys(dt, 0.01 + level / 100_000)
        screen.fill((0, 0, 0))
        player.draw()
        deleter = []
        for i in range(len(missile)):
            if missile[i].collide(player) or player.collide(missile[i]):
                running = False
            if missile[i].draw(dt):
                deleter.append(i)
                score += 1
                img = font.render(f'Score: {score}', True, (255, 255, 255))

        for i in deleter:
            del missile[i]
        screen.blit(img, (screensize[0] / 2 - img.get_width() / 2, screensize[1] * 0.90 - img.get_height() / 2))

    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, int(screensize[0] / 5))
    running = True
    iterator = 0
    frequency = .3
    while running:
        iterator += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        red = int(math.sin(iterator * frequency + 0) * 100 + 155)
        green = int(math.sin(iterator * frequency + 2) * 100 + 155)
        blue = int(math.sin(iterator * frequency + 4) * 100 + 155)
        img = font.render(f'Score: {score}', True, (red, green, blue))
        pygame.display.update((0, 0, screensize[0], screensize[1]))
        screen.blit(img, (screensize[0] / 2 - img.get_width() / 2, screensize[1] / 2 - img.get_height() / 2))
        clock.tick(30)
    pygame.quit()  # quit the screen


if __name__ == '__main__':
    main()
