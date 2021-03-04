from pygame.locals import *
import pygame

nColonne = 30

larghezza = 1500
altezza = 950
nRighe = altezza*nColonne/larghezza
larghezzaQ = larghezza/nColonne
altezzaQ = altezza/nRighe
map1 =\
"""
















qqqqqqqqqqqqqqqqq
qqqqqqqqqqqqqqqqq
"""


def init_display():
    global screen, tileup, tiledown, sfondo
    screen = pygame.display.set_mode((larghezza, altezza))
    sfondo = pygame.image.load("D:\scuola\PCTO\Immagini\Sfondo.png")
    screen.blit(sfondo, (0, 0))
    tileup = pygame.image.load("D:\scuola\PCTO\Immagini\prato.png")
    tiledown = pygame.image.load("D:\scuola\PCTO\Immagini\Terra.png")

def tiles(map1):

    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "w":
                screen.blit(tileup, (x * larghezzaQ, y * altezzaQ))
            if c == "q":
                screen.blit(tiledown, (x * larghezzaQ, y * altezzaQ))


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