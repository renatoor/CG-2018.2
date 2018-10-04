import math
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def FuncaoXY():
    x = 0.0
    y = 0.0
    inc = 0.1

    z = lambda x, y: 0.5 * (- x ** 2) + y ** 2  
    #z = lambda x, y: 0.5 * x ** 2 + y ** 2  

    while y <= 1.0:
        x = 0.0
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(math.cos(x),math.sin(x),math.cos(y))
        glVertex3fv((x, y, z(x, y)))
        while x <= 1.0:
            glVertex3fv((x, y + inc, z(x, y + inc)))
            glVertex3fv((x + inc, y, z(x + inc, y)))
            x += inc
        glVertex3fv((x, y + inc, z(x, y + inc)))
        glEnd()
        y += inc

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    FuncaoXY()
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
