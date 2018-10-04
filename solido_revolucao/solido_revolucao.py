import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def rev(fn_x, fn_y):
    return lambda u, v: (fn_x(u) * math.cos(v), fn_y(u), fn_x(u) * math.sin(v))

def Revolucao():
    r = 1.0
    c = 2.0

    s =  rev(lambda x: c + r * math.cos(x), lambda y: r * math.sin(y))

    delta = 0.0
    phi = 0.0
    inc = 0.1
    max_ = math.pi * 2

    while delta <= max_:
        glBegin(GL_TRIANGLE_STRIP)
        glColor3fv(cores[random.choice(range(len(cores)))])
        phi = 0.0
        while phi <= max_:
            glVertex3fv(s(delta, phi))
            glVertex3fv(s(delta + inc, phi))
            phi += inc
        glVertex3fv(s(delta, 0.0))
        glVertex3fv(s(delta + inc, 0.0))
        glEnd()
        delta += inc

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Revolucao()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
