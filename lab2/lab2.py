from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import sys
import numpy

global xpos  # Величина вращения по оси x
global ypos  # Величина вращения по оси y
global ambient  # рассеянное освещение
global dAmbient
global GREEN
global RED
global WHITE
global bgColor
global lightpos  # Положение источника освещения
global withSource


def init():
    global xpos
    global ypos
    global ambient
    global dAmbient
    global GREEN
    global RED
    global WHITE
    global bgColor
    global lightpos
    global withSource

    withSource = True
    xpos = -0.8
    ypos = 0.0
    dAmbient = 1.0
    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    GREEN = (0.2, 0.8, 0.0, 1)  # green
    RED = (0.8, 0.3, 0.3, 0.5)  # red
    WHITE = (1, 1, 1, 1)
    bgColor = (0.5, 0.5, 0.5, 1.0)
    lightpos = (0.0, 0.0, -1.0)

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    # glLightfv(GL_SPOT_DIRECTION,GL_POSITION,lightpos)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_LIGHT0)
    lighting(withSource)


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xpos
    global ypos
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:  # Клавиша вверх
        ypos += 0.2  # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        ypos -= 0.2  # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        xpos -= 0.2  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        xpos += 0.2  # Увеличиваем угол вращения по оси Y
    glutPostRedisplay()  # Вызываем процедуру перерисовки


def keys(key, x, y):
    global ambient
    global dAmbient
    global withSource

    if ord(key) == ord("-"):
        dAmbient -= 0.2
    if ord(key) == ord("="):
        dAmbient += 0.2
    if ord(key) == ord("s"):
        withSource = not withSource
        print("Source")

    ambient = (dAmbient, 1.0, 1.0, 1.0)
    glutPostRedisplay()


def loadTexture():
    try:
        image = Image.open("texture.jpeg")
    except IOError as ex:
        print('IOError: failed to open texture file')
    textData = numpy.array(list(image.getdata()), numpy.int8)
    textureID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
                 0, GL_RGB, GL_UNSIGNED_BYTE, textData)


def lighting(withSource):
    global xpos
    global ypos
    global lightpos
    lightpos = (xpos, ypos, -1)
    # light source
    if withSource:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, ambient)
        glTranslate(lightpos[0], lightpos[1], 0)
        glutSolidSphere(0.1, 30, 30)
        #
        glTranslate(-lightpos[0], -lightpos[1], 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))
    # light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_LIGHT0)  # Включаем один источник света


def teapot():
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
    glMaterialfv(GL_FRONT, GL_DIFFUSE, GREEN)
    glEnable(GL_CULL_FACE)
    glTranslatef(0.3, 0.0, 0.0)
    glRotatef(20, -1.0, 0.0, 0.0)
    glutSolidTeapot(0.35)
    #
    glTranslatef(-0.3, 0.0, 0.0)
    glRotatef(20, 1.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 0))
    glDisable(GL_CULL_FACE)


def cylinder():
    glMaterialfv(GL_FRONT, GL_DIFFUSE, WHITE)
    glRotatef(250, 1, 0, 0)
    glTranslatef(0, 0, 0.5)
    glEnable(GL_TEXTURE_2D)
    #
    loadTexture()
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    gluCylinder(qobj, 0.2, 0.2, 0.2, 20, 20)
    #
    glRotatef(250, -1, 0, 0)
    glTranslatef(0, 0, -0.5)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 0))
    glDisable(GL_TEXTURE_2D)


def sphere():
    global RED
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, RED)
    glTranslatef(-0.3, 0.0, 0.0)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glutSolidSphere(0.35, 30, 30)
    #
    glDisable(GL_BLEND)
    glTranslatef(0.3, 0.0, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))


# Процедура перерисовки
def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем цветом
    glPushMatrix()  # Сохраняем текущее положение "камеры"
    #
    teapot()
    #
    sphere()
    #
    cylinder()
    #
    lighting(withSource)
    #
    glPopMatrix()  # Возвращаем сохраненное положение "камеры"
    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(950, 950)
glutInitWindowPosition(450, 50)
# Инициализация OpenGl
glutInit(sys.argv)
glutCreateWindow(b"Task 2")
glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)
glutKeyboardFunc(keys)
init()
glutMainLoop()
