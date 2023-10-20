# Камера и передвижение ее в пространстве,
# поставить три фигуры вращения
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

global zAlfa
global xAlfa
global speed
global speed1
global posX
global posY

global s1
global s2

s1 = 0
s2 = 2

posY = posX = 0
speed = speed1 = 0
zAlfa = 180
xAlfa = 50

vertCube = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

vert = [
    1, 1, 0,
    1, -1, 0,
    -1, -1, 0,
    -1, 1, 0
]


def drawCube():
    glPushMatrix()
    glTranslate(3, 3, 1)
    glRotate(s1, s1*0.5, 0, s1*0.5)
    glScale(1, 1, 0.5)
 
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3f(0, 0, 1)
            glVertex3fv(vertCube[vertex])
    glEnd()
    glPopMatrix()


def drawSphere():
    glPushMatrix()
    glTranslate(0, -3, 2)
    glRotate(s1, 0, s1*0.5, 0)
    glScale(1, 1, 1)

    glColor3f(1, 0.3, 0)
    glutWireSphere(1, 20, 20) #(innerRadius, outerRadius, GLint nsides, GLint rings);

    glPopMatrix()
    

def drawTorus():
    glPushMatrix()
    glTranslate(0, -6, 1)
    glRotate(s1, s1*0.5, 0, 0)
    glScale(1, 1, 0.5)

    glColor3f(1, 0.3, 1)
    glutSolidTorus(0.5, 1, 20, 20) #(innerRadius, outerRadius, GLint nsides, GLint rings);

    glPopMatrix()


def showWorld():
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vert)

    # сделаем клеточки
    i = -5
    while i < 5:
        i += 1
        j = -5
        while j < 5:
            glPushMatrix()
            if ((i+j) % 2 == 0):
                glColor3f(0, 0.5, 0)
            else:
                glColor3f(1, 1, 1)

            glTranslatef(i*2, j*2, 0)
            glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
            glPopMatrix()
            j += 1

    glDisableClientState(GL_VERTEX_ARRAY)


def moveCamera():
    global zAlfa
    global xAlfa
    global speed
    global speed1
    global posX
    global posY

    xAlfa = 180 if xAlfa > 180 else xAlfa
    xAlfa = 0 if xAlfa < 0 else xAlfa

    zAlfa = 0 if zAlfa > 360 else zAlfa
    zAlfa = 360 if zAlfa < 0 else zAlfa

    ugol = zAlfa / 180 * -3.14

    if (speed < 0):
        speed = -0.1
    if (speed > 0):
        speed = 0.1
    if (speed != 0):
        posX += sin(ugol) * speed
        posY += cos(ugol) * speed

    if (speed1 < 0):
        speed1 = -0.1
    if (speed1 > 0):
        speed1 = 0.1
    if (speed1 <= -0.1):
        posX += sin(ugol - (3.14 * 0.5)) * speed1
        posY += cos(ugol - (3.14 * 0.5)) * speed1
    if (speed1 >= 0.1):
        posX += sin(ugol - (3.14 * 0.5)) * speed1
        posY += cos(ugol - (3.14 * 0.5)) * speed1

    glRotatef(-xAlfa, 1, 0, 0)
    glRotatef(-zAlfa, 0, 0, 1)
    glTranslatef(-posX, -posY, -3.0)

    speed = 0
    speed1 = 0

    # glTranslate(0, 0, -3)


def keyboard(key, x, y):
    key = key.decode('UTF-8')
    global speed
    global speed1
    if (key == 'w' or key == 'W'):
        speed += 2
    if (key == 's' or key == 'S'):
        speed -= 2
    if (key == 'a' or key == 'A'):
        speed1 += 5
    if (key == 'd' or key == 'D'):
        speed1 -= 5

    glutPostRedisplay()


def sKeyboard(key, x, y):
    global zAlfa
    global xAlfa

    if (key == GLUT_KEY_LEFT):
        zAlfa += 5
    if (key == GLUT_KEY_RIGHT):
        zAlfa -= 5
    if (key == GLUT_KEY_UP):
        xAlfa += 2
    if (key == GLUT_KEY_DOWN):
        xAlfa -= 2
    glutPostRedisplay()


def display():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    moveCamera()
    showWorld()

    drawCube()
    drawTorus()
    drawSphere()
    glPopMatrix()

    glutSwapBuffers()


def loop(count):
    global s1
    global s2
    s1 += 1
    s2 -= 2
    glutPostRedisplay()
    glutTimerFunc(40, loop, 0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500) # устанавливаем размер окна

    # позиция верхнего левого угла окна (начало координат)
    glutInitWindowPosition(100, 200)
    glutCreateWindow('8')  # Пишем заголовок окна

    glFrustum(-1, 1, -1, 1, 2, 180)

    glClearDepth(1.0)  # Глубина фона самая дальняя
    glEnable(GL_DEPTH_TEST)  # Включить глубинное тестирование для z-выбраковки
    glDepthFunc(GL_LEQUAL)

    # Зарегистрировать обработчик обратного вызова для события перерисовки окна
    glutDisplayFunc(display)

    glutKeyboardFunc(keyboard)
    glutSpecialFunc(sKeyboard)

    glutTimerFunc(40, loop, 0)  # Запуск таймера

    glutMainLoop()


main()
