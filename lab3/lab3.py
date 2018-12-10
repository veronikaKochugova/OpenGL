from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy

# http://openglsamples.sourceforge.net/cube2_py.html
from surface import surfaceXY, surfaceYZ, surfaceXZ

WHITE = (1, 1, 1, 1)
GREEN = (0.5, 0.9, 0.0, 1)
withSource = True

smoothing = 0

W = 2
SLICES = 20


def create_planes(N):
    PLANES = []
    PLANES.append(surfaceXY(W, W, -W / 2, N))
    PLANES.append(surfaceXY(W, W, W / 2, N))
    PLANES.append(surfaceYZ(-W / 2, W, W, N))
    PLANES.append(surfaceYZ(W / 2, W, W, N))
    PLANES.append(surfaceXZ(W, W / 2, W, N))
    PLANES.append(surfaceXZ(W, -W / 2, W, N))
    return PLANES


PLANES = create_planes(SLICES)


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, WHITE)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    lighting(withSource)


def lighting(with_source):
    light_pos = (0, 1, 2)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, WHITE)  # light model
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # light source position
    glEnable(GL_LIGHT0)  # light source on


def update(P):
    PP = create_planes(SLICES)
    for p, pp in zip(P, PP):
        for plane, pplane in zip(p, pp):
            for v, vv in zip(plane, pplane):
                R = W / 2
                x = vv[0]
                y = vv[1]
                z = vv[2]
                new_x = x * numpy.sqrt(1 - (y * y / 2) - (z * z / 2) + (y * y * z * z / 3))
                new_y = y * numpy.sqrt(1 - (z * z / 2) - (x * x / 2) + (z * z * x * x / 3))
                new_z = z * numpy.sqrt(1 - (x * x / 2) - (y * y / 2) + (x * x * y * y / 3))
                v[0] = new_x * smoothing + x * (1 - smoothing)
                v[1] = new_y * smoothing + y * (1 - smoothing)
                v[2] = new_z * smoothing + z * (1 - smoothing)
    return P


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, GREEN)

    glTranslatef(0.0, 0.0, -6.0)
    gluLookAt(0, 0, 0, -0.2, -0.4, -1, 0, 1, 0)

    P = PLANES
    P = update(P)

    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    for planes in P:
        for plane in planes:
            for vertex in plane:
                # glTexCoord2f(coord[0], coord[1])
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    lighting(False)
    glutSwapBuffers()


def special_keys(key, x, y):
    global smoothing
    if key == GLUT_KEY_UP:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if key == GLUT_KEY_DOWN:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    if key == GLUT_KEY_LEFT and smoothing > 0:  # Клавиша влево
        smoothing -= 0.1  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT and smoothing < 1:  # Клавиша вправо
        smoothing += 0.1  # Увеличиваем угол вращения по оси Y
    glutPostRedisplay()  # Вызываем процедуру перерисовки


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('Lab3')

    glutDisplayFunc(DrawGLScene)
    glutSpecialFunc(special_keys)
    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
