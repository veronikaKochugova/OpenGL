from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import sys
import numpy

global p_pos_x  # light source shift value on X
global p_pos_y  # light source shift value on Y
global ambient  # light color
global dAmbient
global GREEN
global RED
global WHITE
global withSource

V = [[+0.3, +0.3, +0.3],
     [+0.3, +0.3, -0.3],
     [+0.3, -0.3, -0.3],
     [-0.3, -0.3, -0.3],
     [-0.3, -0.3, +0.3],
     [-0.3, +0.3, +0.3],
     [+0.3, -0.3, +0.3],
     [-0.3, +0.3, -0.3]]

PLANES = [
    (V[2], V[3], V[7], V[1]),  # 1
    (V[6], V[2], V[1], V[0]),  # 2
    (V[4], V[6], V[0], V[5]),  # 3
    (V[3], V[4], V[5], V[7]),  # 4
    (V[6], V[4], V[3], V[2]),  # 5
    (V[5], V[0], V[1], V[7]),  # 6
]

COORDS = ([0, 0], [1, 0], [1, 1], [0, 1])

WINDOW_WIDTH = 740
WINDOW_HEIGHT = 840

teapot_size = 0.35
sphere_size = 2.0


COLOR_R = 1
COLOR_G = 1
COLOR_B = 1

light_x = 50.0
light_y = 20.0
light_z = 30.0

sphere_brightness = 0.50


def init():
    global p_pos_x
    global p_pos_y
    global ambient
    global dAmbient
    global GREEN
    global RED
    global WHITE
    global withSource

    withSource = True
    xpos = -0.8
    ypos = 0.0
    dAmbient = 1.0

    ambient = (1.0, 1.0, 1.0, 1)  # white
    GREEN = (0.2, 0.8, 0.0, 1)  # green
    RED = (0.8, 0.3, 0.3, 0.5)  # red
    WHITE = (1, 1, 1, 1)

    glClearColor(0.0, 0.0, 0.0, 1.0)  # grey background
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # drawing border
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    lighting(withSource)


def special_keys(key, x, y):
    global p_pos_x
    global p_pos_y
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


def load_image():
    image = Image.open("texture.jpeg")

    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def load_texture():
    global image
    try:
        image = Image.open("texture.jpeg")
    except IOError as ex:
        print('IOError: failed to open texture file' + ex)
    text_data = numpy.array(list(image.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, text_data)


def lighting(with_source):
    light_pos = (p_pos_x, p_pos_y, -1)
    # light source
    if with_source:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, ambient)
        glTranslate(light_pos[0], light_pos[1], 0)
        glutSolidSphere(0.1, 30, 30)
        # undo changes
        glTranslate(-light_pos[0], -light_pos[1], 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))
    # light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # light model
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # light source position
    glEnable(GL_LIGHT0)  # light source on


def teapot():
    # Material
    glEnable(GL_CULL_FACE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    #
    glutSolidTeapot(teapot_size)
    # undo changes
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 0))
    glDisable(GL_CULL_FACE)


def cube():
    # Material
    glMaterialfv(GL_FRONT, GL_DIFFUSE, WHITE)
    glEnable(GL_TEXTURE_2D)
    # load_image()
    load_texture()
    #
    #glRotatef(250, 1, 0, 0)
    glTranslatef(0.0, 0.5, 0.0)
    #
    obj = gluNewQuadric()
    gluQuadricTexture(obj, GL_TRUE)
    gluSphere(obj, 0.2, 20, 20)
    # undo changes
    glTranslatef(0, -0.5, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 0))
    glDisable(GL_TEXTURE_2D)


def sphere():
    # Material
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, RED)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    #
    glTranslatef(-0.3, 0.0, 0.0)
    #
    glutSolidSphere(0.35, 30, 30)
    # undo changes
    glDisable(GL_BLEND)
    glTranslatef(0.3, 0.0, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))


def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # clear screen and ad background color
    glPushMatrix()  # save current "camera" position
    #
    teapot()
    #
    sphere()
    #
    cube()
    #
    lighting(withSource)
    #
    glPopMatrix()  # return saved "camera" position
    glutSwapBuffers()  # draw all from buffer


# RGB
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(950, 950)
glutInitWindowPosition(450, 50)
# Init OpenGl
glutInit(sys.argv)
glutCreateWindow(b"Task 2")
glutDisplayFunc(draw)
glutSpecialFunc(special_keys)
glutKeyboardFunc(keys)
init()
#
glutMainLoop()
