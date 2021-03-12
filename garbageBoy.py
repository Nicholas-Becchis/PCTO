import pygame
import random
from pygame.locals import *
from sys import exit

# Inizializziamo Pygame, schermo e clock(per gestire i frame del gioco)
pygame.init()
screen = pygame.display.set_mode((1150, 640), 0, 255)
pygame.display.set_caption("Garbage Boy")
pygame.display.set_icon(pygame.image.load("images\man.png"))
clock = pygame.time.Clock()

man = pygame.image.load("images\man.png")
#manFlip = pygame.image.load("images\manFlip.png")
cig = pygame.image.load("images\cigarette.png")
box = pygame.image.load("images\Box.png")
bottle = pygame.image.load("images\Bottle.png")
juice = pygame.image.load("images\juice.png")
cloud = pygame.image.load("images\cloud.png")
cloud2 = pygame.image.load("images\cloud2.png")
#bench = pygame.image.load("images\Bench.png")
enemy = pygame.image.load("images\enemy2.png")
over = pygame.image.load("images\over.png")
win=pygame.image.load("images\win.png")
font = pygame.font.SysFont("minecraft", 25)
fnt = pygame.font.SysFont("minecraft", 100)
title=pygame.image.load("Images\Title.png")
menu=pygame.image.load("Images\Menu.png")
PLAY="Images\play.png"
QUIT="Images\Quit.png"
BLACK = (0, 0, 0)
WHITE=(255, 255, 255)
cont = 0

# import pdb; pdb.set_trace()
todraw = pygame.sprite.Group()  # instanzio un oggetto di tipo Group
plats = pygame.sprite.Group()
rub = pygame.sprite.Group()
ground = pygame.sprite.Group()
cigar = pygame.sprite.Group()
nemic=pygame.sprite.Group()
game=pygame.sprite.Group()

class MainMenu():
    def __init__(self):
        mmenu = True
        while mmenu:
            screen.blit(menu, (0, 0))
            text=font.render("Main Menu", True, WHITE)
            screen.blit(text, (510, 450))

            buttonPlay=pygame.image.load(PLAY)
            buttonQuit=pygame.image.load(QUIT)

            buttonPlay=screen.blit(buttonPlay, (200, 500))
            buttonQuit=screen.blit(buttonQuit, (850, 500))


            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if buttonPlay.collidepoint(pygame.mouse.get_pos()):
                            mmenu = False
                        if buttonQuit.collidepoint(pygame.mouse.get_pos()):
                            exit()
            pygame.display.update()
            clock.tick(40)


# punteggio
def message(cont):
    contStr = str(cont)
    surf_text = font.render(contStr, True, BLACK)
    screen.blit(surf_text, (20, 53))


# messaggio nemico
def text():
    surf_text = fnt.render("Game Over", True, BLACK)
    screen.blit(surf_text, (450, 320))


# Classe per la creazione delle piattaforme
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((65, 45, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Classe giocatore
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground = False

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 20
        todraw.add(self)
    def update(self):
        self.rect.x += self.move_x
        xcoll()
        self.rect.y += self.move_y
        ycoll()
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Spara(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground = False
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 550
        cigar.add(self)
    def update(self):
        self.rect.x = self.rect.x + 1
        xcollcig()
        self.rect.y += self.move_y
        # ycoll()
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Classe spazzatura
class Rubbish(pygame.sprite.Sprite):
    onground = False
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        rub.add(self)
    def update(self):
        xcollRubbish()
        screen.blit(self.image, (self.rect.x, self.rect.y))


# classe game over
class GameOver(pygame.sprite.Sprite):
    onground = False
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        game.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Classe nemico
class Nemico(pygame.sprite.Sprite):
    onground=False
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=520
        nemic.add(self)
    def update(self):
        xcollenemy()
        screen.blit(self.image, (self.rect.x, self.rect.y))


# creazione della classe per le immagini di sfondo
class background(pygame.sprite.Sprite):
    onground = False
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        ground.add(self)
    def update(self):
        xcollGround()
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Classe contpunteggio
class Box(pygame.sprite.Sprite):
    onground = False
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 20
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# collisioni
def xcoll():
    collision = pygame.sprite.spritecollide(player, plats, False)
    for block in collision:
        if player.move_x > 0:
            player.rect.right = block.rect.left
        if player.move_x < 0:
            player.rect.left = block.rect.right


def ycoll():
    collision = pygame.sprite.spritecollide(player, plats, False)
    player.onground = False
    for block in collision:
        if player.move_y == 0:
            player.onground = True
        if player.move_y < 0:
            player.rect.top = block.rect.bottom
            player.move_y = 0  # serve per evitare l'impressione che il giocatore si "appiccichi" al soffitto
            player.onground = False
        if player.move_y > 0:
            player.rect.bottom = block.rect.top
            player.onground = True

def xcollRubbish():
    collision=pygame.sprite.spritecollide(player, rub, False)  #cerco le rubbish che hanno una collisione col mio sprite
    for block in collision:
        if player.move_x>0 or player.move_x<0:
            global cont
            cont=cont+100
            rub.remove(block)

# collisioni con il nemico
def xcollenemy():
    collision = pygame.sprite.spritecollide(player, nemic,
                                            False)  # cerco le plats che hanno una collisione col mio sprite
    for block in collision:
        if player.move_x > 0 or player.move_x < 0:
            # nemic.remove(nemico)
            #text()
            # todraw.remove(player)
            # cigar.remove(spara)
            # ground.remove(i)
            game=GameOver(win)


# collisioni con le nuvole
def xcollGround():
    collision = pygame.sprite.spritecollide(player, ground,
                                            False)  # cerco le plats che hanno una collisione col mio sprite


# collisioni con i mozziconi
def xcollcig():
    collision=pygame.sprite.spritecollide(player, cigar, False)  #cerco le spara che hanno una collisione col mio sprite
    for block in collision:
        if player.move_x>0 or player.move_x<0:
            #global cont
            #cont=cont+100
            #screen.fill=BLACK
            if cont<500:
                game=GameOver(over)


# collisioni con il nemico
def xcollenemy():
    collision=pygame.sprite.spritecollide(player, nemic, False)  #cerco le plats che hanno una collisione col mio sprite
    for block in collision:
        if player.move_x>0 or player.move_x<0:
            nemic.remove(nemico)
            #text()
            rub.remove()
            #todraw.remove(player)
            #cigar.remove(spara)
            #ground.remove(i)
            game=GameOver(win)


# Costruzione del gioco
def build():
    myx = 0
    myy = 0
    global level, i, o
    level = [
        '                                                          #',
        '                                                          #',
        '                ù   ù   #                 h  ù            #',
        '                        #                                 #',
        '                        #                                 #',
        '                        #                                 #',
        '                        #                                 #',
        '############################################              #',
        '                                                          #',
        '                                                          #',
        '                                                          #',
        '           h                                              #',
        '                                                          #',
        '###############################              ##############',
        '                                                          #',
        '                                                          #',
        '                                                    ù     #',
        '                                                          #',
        '                                             h            #',
        '                                ###########################',
        '                                                          #',
        '                                                          #',
        '                                                          #',
        '                                                          #',
        '                                                          #',
        '#############################################             #',
        '                                                          #',
        '                  +                                       #',
        '                                                          #',
        '                                                          #',
        '                                                          #',
        'yyyyyyyyyy#################################################']
    contRubbish = 0
    contRubbish2 = 0
    contRubbish3 = 0
    """while contRubbish<4:
        global x
        x=random.randint(5, len(level)-1)
        global y
        y=random.randint(0, len(level[0])-1)
        if level[x][y]==' ':
            level[x]=level[x][:y] + 'b' + level[x][y+1:]
            contRubbish=contRubbish+1"""

    while contRubbish2 < 3:
        x = random.randint(5, len(level) - 1)
        y = random.randint(0, len(level[0]) - 1)
        if level[x][y] == ' ':
            level[x] = level[x][:y] + '+' + level[x][y + 1:]
            contRubbish2 = contRubbish2 + 1

    while contRubbish3 < 2:
        x = random.randint(5, len(level) - 1)
        y = random.randint(0, len(level[0]) - 1)
        if level[x][y] == ' ':
            level[x] = level[x][:y] + '*' + level[x][y + 1:]
            contRubbish3 = contRubbish3 + 1

    for r in level:
        for c in r:
            if c == ' ':
                pass
            elif c == 'h':
                i = background(cloud, myx, myy)
            elif c == '#' or c == 'y':
                p = Platform(myx, myy)
            elif c == 'b':
                a = Rubbish(cig, myx, myy)
            elif c == 'h':
                i = background(cloud, myx, myy)
            elif c == 'ù':
                o = background(cloud2, myx, myy)
            elif c == '+':
                h = Rubbish(bottle, myx, myy)
            elif c == '*':
                j = Rubbish(juice, myx, myy)
            myx += 20

        myy += 20
        myx = 0


# Simulazione di gravità
def gravity():
    if not player.onground:
        player.move_y += 1
contPunteggio = Box(box)
player = Player(man)
nemico = Nemico(enemy)
# spara=Spara(cig)
build()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("Sounds\music.mp3"))

MainMenu()

# Ciclo di gioco
while True:
    screen.fill((0, 204, 255))
    gravity()
    message(cont)
    # text()
    # Ciclo eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Uscita
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Viene premuto un tasto
            if event.key == K_UP:  # Su
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\jumping.wav"))
                if player.onground:  # Salta solo se il giocatore è a terra
                    player.move_y = -15
                    player.onground = False
            if event.key == K_LEFT:  # Sinistra
                # player=PlayerFlip(manFlip)
                # player.onground=False
                player.move_x = -5
            if event.key == K_RIGHT:  # Destra
                player.move_x = 5
        if event.type == KEYUP:  # Viene rilasciato un tasto
            if event.key == K_LEFT:
                player.move_x = 0
            if event.key == K_RIGHT:
                player.move_x = 0
        if cont < 200:
            spara = Spara(cig)
        elif cont == 200:
            todraw.remove(spara)
            # spara.rect.x=spara.rect.x + 50
            # if spara.rect.x>1100:
            # spara.rect.x=0

    # Aggiorna tutte le sprites e lo schermo
    todraw.update()
    plats.update()
    rub.update()
    ground.update()
    cigar.update()
    nemic.update()
    game.update()
    pygame.display.update()

    # Faccio in modo che il gioco non vada oltre i 40FPS
    clock.tick(40)