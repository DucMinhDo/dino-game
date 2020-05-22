import pygame
import math
import random
import background
import character
from pygame import mixer

# Basic information of the game
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Dino Game')
pygame.display.set_icon(pygame.image.load(
    r'asset\stegosaurus-dinosaur-cartoon-icon.png'))

# defind variable
score = 0
run = True
delay = 0.01
jump = False
play = True
music = pygame.mixer.music.load(r'asset\music.mp3')
pygame.mixer.music.play(-1)
font = pygame.font.SysFont('Times New Roman', 30, True)
# defined class
# background
theme = background.THEME(pygame.image.load(
    r'asset\background.png'), 0, 0, 150, delay)
sun = background.SUN(pygame.image.load(r'asset\Sun.png'), 300, 0)
cloud = background.CLOUD(pygame.image.load(
    r'asset\Cloud.png'), 500, random.randint(0, 50), 20, delay)

# character
dino = character.DINO(pygame.image.load(
    r'asset\dino.png'), 20, 350, 900, 2200)
VinhHung = character.OBSTACLES([pygame.image.load(r'asset\Untitled3.png'),
                                pygame.image.load(r'asset\Untitled2.png'),
                                pygame.image.load(r'asset\Untitled.png')],
                               500, 370, 350)


def show_Menu():
    win.fill((0, 0, 0))
    theme.move_loop(win)
    sun.spin(win, 0.1)
    cloud.make_cloud(win)

    win.blit(dino.file, (dino.x, dino.y))
    win.blit(VinhHung.character, (VinhHung.x, VinhHung.y))
    VinhHung.move(win, delay)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (20, 20))


# main loop
while run:
    pygame.time.delay(int(delay * 1000))
    if pygame.time.get_ticks() % 20 == 0:
        score += 1
    for event in pygame.event.get():
        run = False if event.type == pygame.QUIT else True
    show_Menu()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        jump = True
    if jump:
        dino.move(delay)
        if dino.y > dino.y0:
            dino.vy = dino.vy0
            jump = False
    if dino.y >= 350 and -50 <= VinhHung.x <= 130:
        run = False
        pass
    if pygame.time.get_ticks() % 10 == 0:
        theme.vx += 10 * delay
        VinhHung.vx += 10 * delay
    pygame.display.update()

pygame.quit()
