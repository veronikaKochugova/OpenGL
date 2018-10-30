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
global color1
global color2
global bgColor
global lightpos  # Положение источника освещения


def init():
    global xpos
    global ypos
    global ambient
    global dAmbient
    global color1
    global color2
    global color3
    global bgColor
    global lightpos

    xpos = 0.0
    ypos = 0.0
    dAmbient = 1.0
    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    color1 = (0.2, 0.8, 0.0, 1)  # green
    color2 = (0.8, 0.3, 0.3, 0.3)  # red
    color3 = (0.5, 0.3, 0.6, 1)
    bgColor = (0.5, 0.5, 0.5, 1.0)
    lightpos = (1.0, 1.0, 1.0)

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    # glLightfv(GL_SPOT_DIRECTION,GL_POSITION,lightpos)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_LIGHT0)


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xpos
    global ypos
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:  # Клавиша вверх
        xpos -= 0.2  # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        xpos += 0.2  # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        ypos -= 0.2  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        ypos += 0.2  # Увеличиваем угол вращения по оси Y
    glutPostRedisplay()  # Вызываем процедуру перерисовки


def keys(key, x, y):
    global ambient
    global dAmbient
    if ord(key) == ord("-"):
        dAmbient -= 0.2
    if ord(key) == ord("="):
        dAmbient += 0.2
    ambient = (dAmbient, 1.0, 1.0, 1.0)
    print(ambient)
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


# Процедура перерисовки
def draw():
    global xpos
    global ypos
    global lightpos
    global color1
    global color2
    global bgColor

    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем цветом
    glPushMatrix()  # Сохраняем текущее положение "камеры"
    lightpos = (1.0, xpos, ypos)
    # glRotatef(xrot, 1.0, 0.0, 0.0)  # Вращаем по оси X на величину xrot
    # glRotatef(yrot, 0.0, 1.0, 0.0)  # Вращаем по оси Y на величину yrot
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Источник света вращаем
    # glDisable(GL_TEXTURE_2D)
    #
    # Рисуем сферу
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, коричневый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, color2)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color2)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glTranslatef(-0.3, 0.0, 0.0)
    glutSolidSphere(0.35, 20, 20)
    glDisable(GL_BLEND)
    #
    #
    # Teapot
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, color1)
    glTranslatef(0.6, 0.0, 0.0)
    glRotatef(20, 1.0, 0.0, 0.0)
    glutSolidTeapot(0.35)
    #
    #
    # Cylinder
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.0, 0.0,
                                                  0.0, 1))
    glTranslatef(-0.3, 0.5, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    loadTexture()
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    gluCylinder(qobj, 0.2, 0.2, 0.2, 20, 20)
    glDisable(GL_TEXTURE_2D)
    #
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
