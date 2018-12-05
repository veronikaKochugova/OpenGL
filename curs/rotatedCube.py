from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy

# http://openglsamples.sourceforge.net/cube2_py.html

WHITE = (1, 1, 1, 1)
xpos = -0.8  # light source shift value on X
ypos = 0.0  # light source shift value on Y
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
CUBE_WIDTH = 0.5

V = [[+CUBE_WIDTH, +CUBE_WIDTH, +CUBE_WIDTH],
     [+CUBE_WIDTH, +CUBE_WIDTH, -CUBE_WIDTH],
     [+CUBE_WIDTH, -CUBE_WIDTH, -CUBE_WIDTH],
     [-CUBE_WIDTH, -CUBE_WIDTH, -CUBE_WIDTH],
     [-CUBE_WIDTH, -CUBE_WIDTH, +CUBE_WIDTH],
     [-CUBE_WIDTH, +CUBE_WIDTH, +CUBE_WIDTH],
     [+CUBE_WIDTH, -CUBE_WIDTH, +CUBE_WIDTH],
     [-CUBE_WIDTH, +CUBE_WIDTH, -CUBE_WIDTH]]

PLANES = [
    (V[2], V[3], V[7], V[1]),  # 1
    (V[6], V[2], V[1], V[0]),  # 2
    (V[4], V[6], V[0], V[5]),  # 3
    (V[3], V[4], V[5], V[7]),  # 4
    (V[6], V[4], V[3], V[2]),  # 5
    (V[5], V[0], V[1], V[7]),  # 6
]

COORDS = ([0, 0], [CUBE_WIDTH, 0], [CUBE_WIDTH, CUBE_WIDTH], [0, CUBE_WIDTH])


def InitGL(Width, Height):
    global xpos
    global ypos
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

    # initialize texture mapping
    glEnable(GL_TEXTURE_2D)

    # light
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    lighting(withSource)


def lighting(with_source):
    light_pos = (xpos, ypos, -0.5)
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

    glTranslatef(0.0, 0.0, -6.0)

    # Draw Cube (multiple quads)
    glBegin(GL_QUADS)
    for plane in PLANES:
        for vertex, coord in zip(plane, COORDS):
            glTexCoord2f(coord[0], coord[1])
            glNormal3f(vertex[0], vertex[1], vertex[2])
            glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    lighting(False)
    glutSwapBuffers()


def load_texture():
    global image
    try:
        image = Image.open("texture.jpeg")
    except IOError as ex:
        print('IOError: failed to open texture file' + ex)
    text_data = numpy.array(list(image.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    #
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    #
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, text_data)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('OpenGL Python Textured Cube')

    glutDisplayFunc(DrawGLScene)
    InitGL(640, 480)
    load_texture()
    glutMainLoop()


if __name__ == "__main__":
    main()
