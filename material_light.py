# Свойства материала
# Создать сцену: две (или больше) фигуры (одна из них вращения) стоят на поверхности. Фигуры освещены
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

s1 = 0

posY = posX = 0
speed = speed1 = 0
zAlfa = 180
xAlfa = 50

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

    glTranslate(0, 0, 2)


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

def showScene():
    glPushMatrix()

    glBegin(GL_QUADS)

    glColor3f(0.5, 0.5, 0.5)
    glVertex3f(-2.5, -2.5, 0)
    glVertex3f(-2.5, 2.5, 0)
    glVertex3f(2.5, 2.5, 0)
    glVertex3f(2.5, -2.5, 0)

    glEnd()

    glPopMatrix()

def showCone():
    mat_dif = [0.0, 0.0, 0.8]
    mat_amb = [0.2, 0.2, 0.2]
    mat_spec = [0.6, 0.6, 0.6]
    mat_shininess = 0.5 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPushMatrix()
    glColor3f(1, 0, 1)
    glTranslatef(0, 0, 1)
    glRotatef(180, 0, 0, 0)
    glutSolidCone(0.5, 1, 20, 20)

    glPopMatrix()

def showTorus(): 
    mat_dif = [0.8, 0.8, 0]
    mat_amb = [0.2, 0.2, 0.2]
    mat_spec = [0.6, 0.6, 0.6]
    mat_shininess = 0.5 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPushMatrix()
    glColor3f(0, 1, 1)
    glTranslatef(-1.5, 1, 0.85 + 0.275)
    glRotatef(90, 1, 0, 0)
    glRotatef(s1, 0, 1, 0)
    glutSolidTorus(0.275, 0.85, 15, 15)
    glPopMatrix()

def showTeapot(): 
    mat_dif = [0.9, 0.2, 0]
    mat_amb = [0.2, 0.2, 0.2]
    mat_spec = [0.6, 0.6, 0.6]
    mat_shininess = 0.5 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPushMatrix()
    glColor3f(0.25, 0.5, 1)
    glTranslatef(-1.5, 1, 0.85 + 0.275)
    glRotatef(90, 1, 0, 0)
    glRotatef(s1 * -2, 0, 1, 0)
    glutSolidTeapot(0.3)
    glPopMatrix()

def display():
    # Очищаем буфер кадра и буфер глубины
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(20, 1, 0, 0)
    moveCamera()

    showScene()

    showTeapot()
    showTorus()
    showCone()

    glPopMatrix()

    glFlush()

def reshape(w, h):
    #Устанавливаем размер области вывода равным размеру окна
    glViewport(0, 0, w, h)

    #задаем матрицу проекции с учетом размеров окна
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(
        40, # угол зрения в градусах
        w / h, # коэффициент сжатия окна
        1, 100  # расстояние до плоскостей отсечения
    )
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0, 0, 8, # положение камеры
        0, 0, 0, # центр сцены
        0, 1, 0 # положительное направление оси y
    )



def loop(count):
    global s1
    s1 +=1

    glutPostRedisplay()
    glutTimerFunc(40, loop, 0)

def init():
    light_ambient = [0, 0, 0, 1]
    light_diffuse = [1, 1, 1, 1]
    light_specular = [1, 1, 1, 1]
    light_position = [1, 1, 1, 0]

    #Устанавливаем параметры источника света
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # включаем освещение и источник света
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)

    # включаем z буфер
    glEnable(GL_DEPTH_TEST)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500) # устанавливаем размер окна

    # позиция верхнего левого угла окна (начало координат)
    glutInitWindowPosition(0, 0)
    glutCreateWindow('PZ_10')  # Пишем заголовок окна

    init()

    # Зарегистрировать обработчик обратного вызова для события перерисовки окна
    glutDisplayFunc(display)

    glutReshapeFunc(reshape)

    glutKeyboardFunc(keyboard)
    glutSpecialFunc(sKeyboard)

    glutTimerFunc(40, loop, 0)  # Запуск таймера

    glutMainLoop()


main()
