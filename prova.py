import pygame
import random
from pygame.locals import *
from sys import exit

# Inizializziamo Pygame, schermo e clock(per gestire i frame del gioco)
pygame.init()
screen=pygame.display.set_mode((1150,640),0,255)
pygame.display.set_caption("")
clock=pygame.time.Clock()
#Creo 2 tipi di "sprites", le piattaforme e l'omino, per gestire le collisioni
global man, bottle
man=pygame.image.load("images\man.png")
bottle=pygame.image.load("images\cigarette.png")
box=pygame.image.load("images\Box.png")
#import pdb; pdb.set_trace()
todraw=pygame.sprite.Group()
plats=pygame.sprite.Group()

#Classe per la creazione delle piattaforme
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill((65,45,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#Classe giocatore
class Player(pygame.sprite.Sprite):
    move_x=0
    move_y=0
    onground=False
    def __init__(self, img):     
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        #self.screen.blit(man, (x * larghezzaQ, y * altezzaQ))
        #self.image=pygame.Surface((10,10))
        #self.image.fill((0,255,0))
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=20
        todraw.add(self)
    def update(self):
        self.rect.x+=self.move_x
        xcoll()
        self.rect.y+=self.move_y
        ycoll()
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
#Classe spazzatura
class Rubbish(pygame.sprite.Sprite):
    onground=False
    def __init__(self,img,Platform):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        #self.image=pygame.Surface((20,20))
        #self.image.fill((65,45,0))
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(20,1100)
        self.rect.y=random.randint(20,620)
        if((self.rect.x,self.rect.y)!=p){

        }
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#Classe contpunteggio
class Box(pygame.sprite.Sprite):
    onground=False
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        #self.image=pygame.Surface((20,20))
        #self.image.fill((65,45,0))
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=20
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))



#collisioni
def xcoll():
    collision=pygame.sprite.spritecollide(player, plats, False)
    for block in collision:
        if player.move_x>0:
            player.rect.right=block.rect.left
        if player.move_x<0:
            player.rect.left=block.rect.right
def ycoll():
        collision=pygame.sprite.spritecollide(player, plats, False)
        player.onground=False
        for block in collision:
            if player.move_y==0:
                player.onground=True
            if player.move_y<0:
                player.rect.top=block.rect.bottom
                player.move_y=0     #serve per evitare l'impressione che il giocatore si "appiccichi" al soffitto
                player.onground=False
            if player.move_y>0:
                player.rect.bottom=block.rect.top
                player.onground=True

#inizializzo un giocatore
#player = Player()
#player = pygame.image.load("images\Bottle.png")

#Costruzione del gioco
def build():
    myx=0
    myy=0
    level=[
            '                                                          ',
            '                                                          ',
            '                        #                                 ',
            '                        #                                 ',
            '                        #                                 ',
            '                        #                                 ',
            '                        #                                 ',
            '############################################             #',
            '      #                                                  #',
            '      #                                                  #',
            '      #                                                  #',
            '      #                                                  #',
            '      #                                                  #',
            '###############################             ##############',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            ' #                             ###########################',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            ' #                                                        ',
            '#############################################             ',
            '                                                          ',
            '                                                          ',
            '                                                          ',
            '                                                          ',
            '                                                          ',
            'yyyyyyyyyy################################################']
    for r in level:
        for c in r:
            if c==' ':
                pass
            elif c=='#'or'y':
                p=Platform(myx,myy)
            #elif c=='b':
                #boxit=Box(myx,myy,box)
            myx+=20
        myy+=20
        myx=0

#Simulazione di gravità
def gravity():
    if not player.onground:
        player.move_y+=1
player=Player(man)
rubbish=Rubbish(bottle)
contPunteggio=Box(box)
build()



#Ciclo di gioco
while True:
    screen.fill((0,204,255))
    gravity()
    #Ciclo eventi
    for event in pygame.event.get():
        if event.type==QUIT:  #Uscita
            exit()
        if event.type==KEYDOWN: #Viene premuto un tasto
            if event.key==K_UP:   #Su
                if player.onground:   #Salta solo se il giocatore è a terra
                    player.move_y=-15
                    player.onground=False
            if event.key==K_LEFT: #Sinistra
                player.move_x=-5
            if event.key==K_RIGHT:   #Destra
                player.move_x=5
        if event.type==KEYUP:  #Viene rilasciato un tasto
            if event.key==K_LEFT:
                player.move_x=0
            if event.key==K_RIGHT:
                player.move_x=0

    #Aggiorna tutte le sprites e lo schermo
    todraw.update()
    plats.update()
    pygame.display.update()

    #Faccio in modo che il gioco non vada oltre i 30FPS
    clock.tick(40)