import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Dodecahedron():
    vertices = []
    phiaa = 52.62263590
    phibb = 10.81231754
    r = 1.0
    phia = math.pi*phiaa/180.0
    phib = math.pi*phibb/180.0
    phic = math.pi*(-phibb)/180.0
    phid = math.pi*(-phiaa)/180.0
    the72 = math.pi*72.0/180
    theb = the72/2.0
    the = 0.0

    for i in range(5):
        vertices.append((r*math.cos(the)*math.cos(phia), r*math.sin(the)*math.cos(phia), r*math.sin(phia)))
        the = the+the72

    the=0.0

    for i in range(5, 10):
        vertices.append((r*math.cos(the)*math.cos(phib), r*math.sin(the)*math.cos(phib), r*math.sin(phib)))
        the = the+the72

    the = theb

    for i in range(10, 15):
        vertices.append((r*math.cos(the)*math.cos(phic), r*math.sin(the)*math.cos(phic), r*math.sin(phic)))
        the = the+the72

    the = theb

    for i in range(15, 20):
        vertices.append((r*math.cos(the)*math.cos(phid), r*math.sin(the)*math.cos(phid), r*math.sin(phid)))
        the = the+the72

    def polygon(v1, v2, v3, v4, v5):
        glBegin(GL_POLYGON)
        glColor3fv(cores[random.choice(range(len(cores)))])
        glVertex3fv(vertices[v1])
        glVertex3fv(vertices[v2])
        glVertex3fv(vertices[v3])
        glVertex3fv(vertices[v4])
        glVertex3fv(vertices[v5])
        glEnd()

    polygon(0,1,2,3,4)
    polygon(0,1,6,10,5)
    polygon(1,2,7,11,6)
    polygon(2,3,8,12,7)
    polygon(3,4,9,13,8)
    polygon(4,0,5,14,9)
    polygon(15,16,11,6,10)
    polygon(16,17,12,7,11)
    polygon(17,18,13,8,12)
    polygon(18,19,14,9,13)
    polygon(19,15,10,5,14)
    polygon(15,16,17,18,19)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Dodecahedron()
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
