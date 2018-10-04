import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Prisma():
    vertices = []
    top_vertices = []

    n = 6 
    perc = 0.6

    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    for i in range(n):
        alpha = i * math.pi / (n / 2.0) - (math.pi / 2)
        x = math.cos(alpha)
        z = math.sin(alpha)
	vertices.append((x, -1.0, z))
        glVertex3f(x, -1.0, z)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    for i in range(n):
        alpha = i * math.pi / (n / 2.0) - (math.pi / 2)
        x = math.cos(alpha)
        z = math.sin(alpha)
        height = -1.0 + (2 * perc)
        top_vertices.append((x * (1 - perc), height, z * (1 - perc)))
        glVertex3f(x * (1 - perc), height, z * (1 - perc))

    glEnd()

    for i in range(n):
        glBegin(GL_POLYGON)
        glColor3fv(cores[i % len(cores)])
	glVertex3fv(top_vertices[i])
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[(i + 1) % n])
	glVertex3fv(top_vertices[(i + 1) %n])
        glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Prisma()
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


