from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(1, 0, 1, 0)
    glutWireTeapot(0.5)
    glFlush()
def procMouse(btn,state,x,y):
	st = 'pressed' if(state == GLUT_DOWN) else 'released'
	print('MOTION RECALL:')
	print('button %s %s'%(btn,st))
	print('MOUSE:%s,%s'%(x,y))
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow(b"First")
glutMouseFunc(procMouse)
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
