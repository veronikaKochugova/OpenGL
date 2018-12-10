from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy

# http://openglsamples.sourceforge.net/cube2_py.html
from surface import surfaceXY, surfaceYZ, surfaceXZ

WHITE = (1, 1, 1, 1)
p_pos_x = -0.8  # light source shift value on X
p_pos_y = 0.0  # light source shift value on Y
ambient = WHITE  # light color
dAmbient = 1.0
withSource = True

window = 0
ID = 0

# rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

DIRECTION = 1
CUBE_WIDTH = 0.3

N = 10
PLANES = []
PLANES.append(surfaceXY(1, 1, 0, N))
PLANES.append(surfaceXY(1, 1, 1, N))
PLANES.append(surfaceYZ(1, 1, 1, N))
PLANES.append(surfaceYZ(0, 1, 1, N))
PLANES.append(surfaceXZ(1, 1, 1, N))
PLANES.append(surfaceXZ(1, 0, 1, N))


def InitGL(Width, Height):
    global p_pos_x
    global p_pos_y
    global ambient
    global dAmbient
    global withSource

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
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    lighting(withSource)


def lighting(with_source):
    light_pos = (p_pos_x, p_pos_y, -0.5)
    # light source
    if with_source:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, ambient)
        glTranslate(light_pos[0], light_pos[1], light_pos[2])
        glutSolidSphere(0.1, 30, 30)
        # undo changes
        glTranslate(-light_pos[0], -light_pos[1], 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))
    # light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # light model
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # light source position
    glEnable(GL_LIGHT0)  # light source on


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -4.0)
    gluLookAt(0, 0, 0, -0.2, -0.4, -1, 0, 1, 0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    for planes in PLANES:
        for plane in planes:
            for vertex in plane:
                # glTexCoord2f(coord[0], coord[1])
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    lighting(False)
    glutSwapBuffers()


def special_keys(key, x, y):
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
