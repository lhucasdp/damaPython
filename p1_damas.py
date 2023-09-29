from OpenGL.GL import *
import pygame 
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLUT import *

xPos = 0
yPos = 0
posX = 0

#config
WIDTH, HEIGHT = 401, 401

MATRIZ =[
    [0, 1, 0, 0, 0, 2, 0, 2],
    [1, 0, 1, 0, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 2, 0, 2],
    [1, 0, 1, 0, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 2, 0, 2],
    [1, 0, 1, 0, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 2, 0, 2],
    [1, 0, 1, 0, 0, 0, 2, 0],
]

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

def desenha_peca(x, y, color):
    glBegin(GL_QUADS)
    glColor3fv(color)
    glVertex2f((10 + x), 10 + y)
    glVertex2f((40 + x), 10 + y)
    glVertex2f((40 + x), 40 + y)
    glVertex2f((10 + x), 40 + y)
    glEnd()

def quadrado(x, y, color):
    glBegin(GL_QUADS)
    glColor3fv(color)
    glVertex2f((0 + x), 0 + y)
    glVertex2f((50 + x), 0 + y)
    glVertex2f((50 + x), 50 + y)
    glVertex2f((0 + x), 50 + y)
    glEnd()

def movimenta_peca():
    print()

def peca():
    x=0
    y=0
    global MATRIZ
    for x in range(8):
        for y in range(8):
            if MATRIZ[x][y]==1:
                desenha_peca(x*50, y*50, (0,255,0))
            if MATRIZ[x][y]==2:
                desenha_peca(x*50, y*50, (255,0,0))

def tabuleiro():
    contX = 0
    contY = 0
    global MATRIZ
    for x in range(0, 401, 50):
        contX += 1
        if (contX%2==0):
                quadrado(x, y, (0,0,0))
        for y in range(0, 401, 50):
            contY += 1
            if (contY%2==0):
                quadrado(x, y, (0,0,0))



def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    tabuleiro()
    peca()
    glutSwapBuffers()

def reshape(width, height):
    glutReshapeWindow(WIDTH, HEIGHT)

def mouse_handler(button, state, posX, posY):
    global MATRIZ
    estado = 0
    x= int(posX/50)

    if (int(posY/50)==0):
        y=7
    if (int(posY/50)==1):
        y=6
    if (int(posY/50)==2):
        y=5
    if (int(posY/50)==3):
        y=4
    if (int(posY/50)==4):
        y=3
    if (int(posY/50)==5):
        y=2
    if (int(posY/50)==6):
        y=1
    if (int(posY/50)==7):
        y=0

    if (state==0 and MATRIZ[x][y]==1):
        MATRIZ[x][y]=0
        estado=1
    elif ((state==1) and (MATRIZ[x][y]==0)):
        MATRIZ[x][y]=1


    for i in MATRIZ:
        print(i)
    print(state)
    print(x)
    print(y)
    

    





def main():
    pygame.display.set_mode((1,1), DOUBLEBUF|OPENGL)
    glutInit()
    glutMouseFunc(mouse_handler)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b'DAMAS')

    glOrtho(0, WIDTH, 0, HEIGHT, -50, 1)

    glutDisplayFunc(draw)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glutMouseFunc(mouse_handler)
    global MATRIZ
    for x in MATRIZ:
        print(x)


    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()

