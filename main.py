from pygame.locals import *
import pygame
import sys
import cv2
import numpy as np




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

cap = cv2.VideoCapture(1)

def motionDet():
    #face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


    ret, frame1=cap.read()
    ret, frame2=cap.read()





    diff=cv2.absdiff(frame1, frame2)
    gray=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh=cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=3)
    contours, _=cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<1000:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed", frame1)
    frame1=frame2
    ret, frame2=cap.read()
    if cv2.waitKey(40)==27:
        break




def motionEv():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_RIGHT):
            boyX += boyVelX
        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_LEFT):
            boyX -= boyVelX
        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_UP):
            if boyY == 595:
                boyY -= 200
                boyVelY = 0

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
    boyX,boyY=100,595
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
    pygame.display.set_caption('Garbage Boy')
    pygame.display.set_icon(boy)





    while True:
        boyVelY+=10
        boyY+=boyVelY

        if boyY>595:
            boyY=595

        motionDet()
        motionEv()
        draw()
        reload()



if __name__=="__main__":
    main()