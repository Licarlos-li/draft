import numpy as np 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Demo:
    def __init__(self):
        glutInit()      #启动glut
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(400,400)
        glutCreateWindow(b"OpenGL")             #设定标题
        glutDisplayFunc(self.draw_polygon)     #绘制函数
        self.init_condition()       #设定背景
        glutMainLoop()

    def init_condition(self):
        glClearColor(1.0,1.0,1.0,0.0)
        gluOrtho2D(-8.0,8.0,-8.0,8.0)

    def render(self):
        pass

    def draw_geometry(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_QUADS)
        glVertex2f(-2,2)
        glVertex2f(-2,5)
        glVertex2f(-5,5)
        glVertex2f(-5,2)
        glEnd()
        glFlush()

    def draw_polygon(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)  # 设定颜色RGB
        glBegin(GL_LINES)
        datas = [-2.5+i*0.25 for i in range(21)]
        for i in datas:
            glVertex3f(i,0,2.5)
            glVertex3f(i,0,-2.5)
            glVertex3f(2.5,0,i)
            glVertex3f(-2.5,0,i)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(1,1,1)
        glVertex3f(0,2,0)
        glColor3f(1, 0, 0)
        glVertex3f(-1, 0, 1)
        glColor3f(0, 1, 0)
        glVertex3f(1, 0, 1)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, -1.4)
        glColor3f(1, 1, 1)
        glVertex3f(0, 2, 0)
        glColor3f(1, 0, 0)
        glVertex3f(-1, 0, 1)
        glEnd()
        glFlush()
if __name__ == '__main__':
    Demo()
        