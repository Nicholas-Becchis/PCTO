import pygame
import sys



DIMENSIONI=(1500,950)
BIANCO=(255,255,255)
SFONDO='D:\Scuola\PCTO\Images\Sfondo.png'
BOY='D:\Scuola\PCTO\Images\Man.png'
BOYRUN='D:\Scuola\PCTO\Immages\Man_run.png'
TITLE='D:\Scuola\PCTO\Images\Title.png'
BOTTLE='D:\Scuola\PCTO\Images\Bottle'
ENEMY='D:\Scuola\PCTO\Images\Enemy.png'
GROUND='D:\Scuola\PCTO\Images\Ground.png'
MENU='D:\Scuola\PCTO\Images\Menu.png'


def draw():
    schermo.blit(sfondo, (0, 0))
    schermo.blit(ground, (0, 100))
    schermo.blit(boy, (boyX, boyY))



def reload():
    pygame.display.update()
    pygame.time.Clock().tick(fps)



def main():

    pygame.init()
    global title
    global menu
    global sfondo
    global ground
    global boy, boyX, boyY, boyVelX, boyVelY
    boyX,boyY=-400,25
    boyVelX=20
    boyVelY=0

    title = pygame.image.load(TITLE)
    menu = pygame.image.load(MENU)
    sfondo = pygame.image.load(SFONDO)
    ground = pygame.image.load(GROUND)
    boy = pygame.image.load(BOY)

    global fps
    fps=50
    global schermo
    schermo = pygame.display.set_mode(DIMENSIONI)



    while True:
        boyVelY+=15
        boyY+=boyVelY

        if boyY>25:
            boyY=25

        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            if keys[K_LEFT]

            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type==pygame.KEYDOWN
                and event.key==pygame.K_RIGHT):
                boyX+=boyVelX
            if (event.type==pygame.KEYDOWN
                and event.key==pygame.K_LEFT):
                boyX-=boyVelX
            if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_UP):
                if boyY==25:
                    boyY -= 300
                    boyVelY = 0
        draw()
        reload()



if __name__=="__main__":
    main()