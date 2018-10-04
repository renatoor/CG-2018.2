import math
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Piramide():
    top_vertex = (0, 1, 0)
    vertexes = []

    n = 10 

    glBegin(GL_POLYGON)

    glColor3f(0.0, 1.0, 0.0)

    for i  in range(n):
        alpha = i * math.pi / (n / 2.0) - (math.pi / 2)
        x = math.cos(alpha)
        z = math.sin(alpha)
        vertex = (x, -1.0, z)
	vertexes.append(vertex)
        glVertex3f(x, -1.0, z)

    glEnd()

    for i in range(n):
        glBegin(GL_TRIANGLES)
        glColor3fv(cores[i % len(cores)])
	glVertex3fv(top_vertex)
        glVertex3fv(vertexes[i])
        glVertex3fv(vertexes[(i + 1) % n])
        glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
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


