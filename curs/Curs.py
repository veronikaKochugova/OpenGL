from curs.Cube import *
from curs.NotConvex import *
import numpy

# http://openglsamples.sourceforge.net/cube2_py.html

R = 1
l_pos_x = 1  # light source shift value on X
l_pos_y = 2  # light source shift value on Y
p_pos_x = 0  # polygon shift value on X
withSource = True

SURFACE_WIDTH = 10
SURFACE = [(-SURFACE_WIDTH, -0.5, -SURFACE_WIDTH),
           (SURFACE_WIDTH, -0.5, -SURFACE_WIDTH),
           (SURFACE_WIDTH, -0.5, SURFACE_WIDTH),
           (-SURFACE_WIDTH, -0.5, SURFACE_WIDTH)]

global cube
global not_convex


def InitGL(Width, Height):
    global ambient
    global dAmbient
    global withSource

    global cube
    global not_convex

    cube = Cube()
    not_convex = NotConvex()

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # light
    # glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SINGLE_COLOR)
    # glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, WHITE)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    glEnable(GL_NORMALIZE)
    lighting(withSource)

    draw()


def lighting(with_source):
    light_pos = (l_pos_x, l_pos_y, 1)
    # light source
    if with_source:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, WHITE)
        glTranslate(light_pos[0], light_pos[1], light_pos[2])
        #
        glutSolidSphere(0.1, 30, 30)
        # undo changes
        glTranslate(-light_pos[0], -light_pos[1], -light_pos[2])
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))
    # light
    # glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 90)
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (1,0,0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # light source position
    glEnable(GL_LIGHT0)  # light source on


def special_keys(key, x, y):
    global p_pos_x
    global p_pos_y
    if key == GLUT_KEY_LEFT:
        p_pos_x -= 0.1
        t = -0.05
    if key == GLUT_KEY_RIGHT:
        p_pos_x += 0.1
        t = +0.05
    not_convex.position(t)
    glutPostRedisplay()


def keys(key, x, y):
    global withSource
    global tmp
    global l_pos_x
    global l_pos_y

    if ord(key) == ord("w"):  # Клавиша вверх
        l_pos_y += 0.2  # Уменьшаем угол вращения по оси Х
    if ord(key) == ord("s"):  # Клавиша вниз
        l_pos_y -= 0.2  # Увеличиваем угол вращения по оси Х
    if ord(key) == ord("a"):  # Клавиша влево
        l_pos_x -= 0.2  # Уменьшаем угол вращения по оси Y
    if ord(key) == ord("d"):  # Клавиша вправо
        l_pos_x += 0.2  # Увеличиваем угол вращения по оси Y
    if ord(key) == ord("q"):
        withSource = not withSource
        print("Source")

    glutPostRedisplay()


def surface():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, GREEN)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, GREEN_l)
    glBegin(GL_QUADS)
    for vertex in SURFACE:
        # glTexCoord2f(coord[0], coord[1])
        D = SURFACE_WIDTH * 2
        glNormal3f(vertex[0] / D, vertex[1] / D, vertex[2] / D)
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -6.0)
    gluLookAt(0, 0, 0, -0.2, -0.4, -1, 0, 1, 0)
    #
    surface()
    #
    cube.draw()
    #
    not_convex.draw()
    #
    lighting(withSource)
    glutSwapBuffers()


def idle():
    t = numpy.pi / 20 - 0.006 * (not_convex.unit * not_convex.rotation_limit + not_convex.rotation_times)
    not_convex.position(t)
    glutPostRedisplay()


def main():
    window_size = [1200, 900]
    #
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(*window_size)
    glutInitWindowPosition(250, 100)
    glutCreateWindow('Curs')

    glutIdleFunc(idle)
    glutDisplayFunc(draw)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keys)
    InitGL(*window_size)
    glutMainLoop()


if __name__ == "__main__":
    main()
