from pygame.locals import *
import pygame


map1 = """                             















































w    w    w    w    w    w             w    w    w    w    w    w    w    w    w    w    w    w

q    q    q    q    q    q             q    q    q    q    q    q    q    q    q    q    q    q




q    q    q    q    q    q             q    q    q    q    q    q    q    q    q    q    q    q
"""


def init_display():
    global screen, tileup, tiledown, sfondo
    screen = pygame.display.set_mode((1500, 950))
    sfondo = pygame.image.load("D:\scuola\PCTO\Immagini\Sfondo.png")
    screen.blit(sfondo, (0, 0))
    tileup = pygame.image.load("D:\scuola\PCTO\Immagini\prato.png")
    tiledown = pygame.image.load("D:\scuola\PCTO\Immagini\Terra.png")

def tiles(map1):

    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "w":
                screen.blit(tileup, (x * 16, y * 16))
            if c == "q":
                screen.blit(tiledown, (x * 16, y * 16))


map1 = map1.splitlines()
pygame.init()
init_display()
loop = 1
while loop:

    # screen.fill((0, 0, 0))
    tiles(map1)
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0

    pygame.display.update()
pygame.quit()