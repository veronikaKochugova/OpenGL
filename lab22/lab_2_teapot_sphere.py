from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import sys

WINDOW_WIDTH = 740
WINDOW_HEIGHT = 840

teapot_size = 1.0
sphere_size = 2.0


COLOR_R = 1
COLOR_G = 1
COLOR_B = 1

light_x = 50.0
light_y = 20.0
light_z = 30.0

sphere_brightness = 0.50

# V = [[+1, +1, +1],  # 0
#      [+1, -1, -1],  # 1
#      [-1, +1, -1],  # 2
#      [-1, -1, +1]   # 3
#     ]
#
# PLANES = [
#     (V[0], V[1], V[2]),  # 1
#     (V[3], V[1], V[2]),  # 2
#     (V[3], V[0], V[1]),  # 3
#     (V[3], V[0], V[2]),  # 4
# ]
#
# COORDS = ([0, 0], [1, 0], [0.5, 1])
V = [[+1, +1, +1],
     [+1, +1, -1],
     [+1, -1, -1],
     [-1, -1, -1],
     [-1, -1, +1],
     [-1, +1, +1],
     [+1, -1, +1],
     [-1, +1, -1]]

PLANES = [
    (V[2], V[3], V[7], V[1]),  # 1
    (V[6], V[2], V[1], V[0]),  # 2
    (V[4], V[6], V[0], V[5]),  # 3
    (V[3], V[4], V[5], V[7]),  # 4
    (V[6], V[4], V[3], V[2]),  # 5
    (V[5], V[0], V[1], V[7]),  # 6
]

COORDS = ([0, 0], [1, 0], [1, 1], [0, 1])

rotate_x = 0.0
rotate_y = 0.0
rotate_z = 0.0
steps = [0.1, 0.1, 0.05]


def init_gl(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # glClearDepth(1.0)

    # glDepthFunc(GL_LESS)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)

    # glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)

    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def display():
    global sphere_brightness
    global COLOR_R, COLOR_G, COLOR_B
    global light_x, light_y, light_z
    global rotate_x, rotate_y, rotate_z

    glPushMatrix()

    light = GL_LIGHT0
    glLightfv(light, GL_POSITION, [light_x, light_y, light_z, 0])
    glLightfv(light, GL_DIFFUSE, [COLOR_R, COLOR_G, COLOR_B, 0.0])
    glEnable(light)

    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    gluLookAt(5, 3, 5,
              1, 0, 0,
              0, 1, 0)
    glColor3f(0.8, 0.2, 0.1)
    glScalef(1.0, 1.0, 1.0)

    # teapot
    glEnable(GL_CULL_FACE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

    glutSolidTeapot(teapot_size)


    # glDepthMask(GL_FALSE)

    glDisable(GL_CULL_FACE)
    # glDisable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))

    # sphere
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, 0.5])
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)

    glutSolidSphere(sphere_size, 20, 20)

    # glDepthMask(GL_TRUE)
    glDisable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))

    # cube

    glEnable(GL_TEXTURE_2D)
    glTranslatef(0.0, 0.0, -4.0)
    #
    # glRotatef(rotate_x, 1.0, 0.0, 0.0)
    # glRotatef(rotate_y, 0.0, 1.0, 0.0)
    # glRotatef(rotate_z, 0.0, 0.0, 1.0)
    load_image()
    # draw Tetrahedron
    glBegin(GL_QUADS)
    for plane in PLANES:
        for vertex, coord in zip(plane, COORDS):
            glTexCoord2f(coord[0], coord[1])
            glVertex3f(vertex[0], vertex[1], vertex[2])

    glEnd()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()


def reshape(x, y):
    if y == 0 or x == 0:
        return
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, x/y, 0.5, 20.0)
    glViewport(0, 0, x, y)


def keyboard(key, x, y):
    global light_x, light_y, light_z

    step = 2.0
    if key == GLUT_KEY_LEFT:
        light_x += step
    if key == GLUT_KEY_RIGHT:
        light_x -= step

    if key == GLUT_KEY_UP:
        light_z += step
    if key == GLUT_KEY_DOWN:
        light_z -= step

    if key == GLUT_KEY_PAGE_UP:
        light_y -= step
    if key == GLUT_KEY_PAGE_DOWN:
        light_y += step

    glutPostRedisplay()


def keys(key, x, y):
    global sphere_brightness
    global COLOR_R, COLOR_G, COLOR_B
    global rotate_x, rotate_y, rotate_z

    step = 0.05
    if ord(key) == ord("="):
        if sphere_brightness < 1.0:
            sphere_brightness += step
    if ord(key) == ord("-"):
        if sphere_brightness > 0.0:
            sphere_brightness -= step

    if ord(key) == ord("r"):
        COLOR_R = 0 if COLOR_R == 1 else 1
    if ord(key) == ord("g"):
        COLOR_G = 0 if COLOR_G == 1 else 1
    if ord(key) == ord("b"):
        COLOR_B = 0 if COLOR_B == 1 else 1

    step = 2.0
    if ord(key) == ord("a"):
        rotate_y += step
    if ord(key) == ord("d"):
        rotate_y -= step

    if ord(key) == ord("w"):
        rotate_x += step
    if ord(key) == ord("s"):
        rotate_x -= step

    if ord(key) == ord("q"):
        rotate_z -= step
    if ord(key) == ord("e"):
        rotate_z += step

    glutPostRedisplay()


def load_image():
    image = Image.open("wall.png")

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


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(1000, 800)
    glutCreateWindow("Teapot and sphere")

    init_gl(WINDOW_HEIGHT, WINDOW_WIDTH)

    glLoadIdentity()
    glutDisplayFunc(display)
    # glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard)
    glutKeyboardFunc(keys)
    glutMainLoop()
