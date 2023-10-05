# Написать программу с использованием функций библиотек OGL,
# которая рисует в окне две разноцветные объемные фигуры.
# Фигуры должны вращаться в разные стороны вокруг оси X. 

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glRotated(1, 1, 0, 0)

    # Красный квадрат, нижнее ребро на оси x = 0
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    glVertex3f(10, 0, 0)
    glVertex3f(30, 0, 0)
    glVertex3f(30, 20, 0)
    glVertex3f(10, 20, 0)

    glColor3f(0, 0, 1)
    glVertex3f(10, 20, 20)
    glVertex3f(30, 20, 20)
    glVertex3f(30, 0, 20)
    glVertex3f(10, 0, 20)
    glEnd()

    glRotated(1, 1, 0, 0)

    # Красный квадрат, нижнее ребро на оси x = -5
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    glVertex3f(-20, -5, 0)
    glVertex3f(0, -5, 0)
    glVertex3f(0, 15, 0)
    glVertex3f(-20, 15, 0)
    glEnd()


    glFlush()
    glutSwapBuffers()

def loop(count):
    glutPostRedisplay()
    glutTimerFunc(40, loop, 0)


def initGL():
    glClearColor(0.0, 0.1, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 0.1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(600, 600)   # устанавливаем размер окна
    
    glutInitWindowPosition(50, 50) # позиция верхнего левого угла окна (начало координат)
    glutCreateWindow('Тор вращается вокруг оси X') # Пишем заголовок окна

    glutDisplayFunc(display) # Зарегистрировать обработчик обратного вызова для события перерисовки окна

    glutTimerFunc(40, loop, 0)

    initGL() # Our own OpenGL initialization

    glutMainLoop()


main()