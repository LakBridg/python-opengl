# Написать программу с использованием функций библиотек OGL,
# которая рисует в окне две разноцветные объемные фигуры.
# Фигуры должны вращаться в разные стороны вокруг оси X. 

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Angle:
    def __init__(self, speed):
        self.value = 0
        self.speed = speed
    def next(self):
        self.value += self.speed

triangle = Angle(2)
cube = Angle(-2)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(triangle.value, 1, 0, 0)
    triangle.next()

    # Пирамада
    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 0.0, 1)
    glVertex3f(0.2, -0.1, 0.2)
    glVertex3f(0.4, -0.1, 0.2)
    glVertex3f(0.3, 0.0, 0.4)

    glColor3f(0.0, 1, 0.0)
    glVertex3f(0.3, 0.0, 0.4)
    glVertex3f(0.4, -0.1, 0.2)
    glVertex3f(0.3, 0.1, 0.2)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.3, 0.1, 0.2)
    glVertex3f(0.3, 0.0, 0.4)
    glVertex3f(0.2, -0.1, 0.2)

    glColor3f(1, 1, 1)
    glVertex3f(0.3, 0.1, 0.2)
    glVertex3f(0.2, -0.1, 0.2)
    glVertex3f(0.4, -0.1, 0.2)

    glEnd()

    #Куб(с 4-мя сторонами)
    glLoadIdentity()

    glRotatef(cube.value, 1, 0, 0)
    cube.next()

    glBegin(GL_QUADS)

    glColor3f(0, 0, 1)
    glVertex3f(-0.2, 0.1, 0.2)
    glVertex3f(-0.4, 0.1, 0.2)
    glVertex3f(-0.4, -0.1, 0.2)
    glVertex3f(-0.2, -0.1, 0.2)

    glColor3f(1, 0, 0)
    glVertex3f(-0.2, 0.1, 0.2)
    glVertex3f(-0.4, 0.1, 0.2)
    glVertex3f(-0.4, 0.1, 0.0)
    glVertex3f(-0.2, 0.1, 0.0)

    glColor3f(0, 1, 0)
    glVertex3f(-0.2, -0.1, 0.2)
    glVertex3f(-0.4, -0.1, 0.2)
    glVertex3f(-0.4, -0.1, 0.0)
    glVertex3f(-0.2, -0.1, 0.0)

    glColor3f(1, 1, 1)
    glVertex3f(-0.2,  0.1, 0.0)
    glVertex3f(-0.4,  0.1, 0.0)
    glVertex3f(-0.4, -0.1, 0.0)
    glVertex3f(-0.2, -0.1, 0.0)

    glEnd()

    #Координата x
    glLoadIdentity()
    glBegin(GL_LINES)

    glColor3f(1, 1, 1)
    glVertex3f(-1, 0, 0)
    glVertex3f(1, 0, 0)

    glEnd()

    glFlush() # принудительно выполняет функции OpenGL в конечное время.
    glutSwapBuffers()

def loop(count):
    glutPostRedisplay()
    glutTimerFunc(40, loop, 0)


def initGL():
    glClearColor(0.0, 0, 0.0, 1) # Фон

    #Настройка глубины
    glClearDepth(1.0) # Глубина фона самая дальняя 
    glEnable(GL_DEPTH_TEST) # Включить глубинное тестирование для z-выбраковки
    glDepthFunc(GL_LEQUAL) # Нужно включить тест глубины, чтобы удалить\скрытую поверхность, и установить функцию, используемую для теста глубины

    glMatrixMode(GL_MODELVIEW) # Установка матрица
    glLoadIdentity()
    gluLookAt(150, 150, 150, 0, 0, 0, 0, 100, 0)

def main(): # Инициализация glut
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(600, 600)   # устанавливаем размер окна
    
    glutInitWindowPosition(50, 50 ) # позиция верхнего левогоугла окна (начало координат)
    glutCreateWindow('Две объемные фигуры вращаться в разные стороны вокруг оси X') # Пишем заголовок окна

    glutDisplayFunc(display) # Зарегистрировать обработчик обратного вызова для события перерисовки окна

    glutTimerFunc(40, loop, 0) # Запуск таймера

    initGL() # Настройка GL

    glutMainLoop()


main()
