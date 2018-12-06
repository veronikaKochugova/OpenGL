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
CUBE_WIDTH = 0.3

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


def slicing():
    n = 2
    w = CUBE_WIDTH / n
    #
    vertices = []

    def edgeFlagCallback(param1, param2):
        pass

    def beginCallback(param=None):
        vertices = []

    def vertexCallback(vertex, otherData=None):
        vertices.append(vertex[:2])

    def combineCallback(vertex, neighbors, neighborWeights, out=None):
        out = vertex
        return out

    def endCallback(data=None):
        pass

    tess = gluNewTess()
    gluTessProperty(tess, GLU_TESS_WINDING_RULE, GLU_TESS_WINDING_ODD)
    gluTessCallback(tess, GLU_TESS_EDGE_FLAG_DATA,
                    edgeFlagCallback)  # forces triangulation of polygons (i.e. GL_TRIANGLES) rather than returning triangle fans or strips
    gluTessCallback(tess, GLU_TESS_BEGIN, beginCallback)
    gluTessCallback(tess, GLU_TESS_VERTEX, vertexCallback)
    gluTessCallback(tess, GLU_TESS_COMBINE, combineCallback)
    gluTessCallback(tess, GLU_TESS_END, endCallback)

    tess = gluNewTess()
    gluTessBeginPolygon(tess, 0)
    for polygon in PLANES:
        gluTessBeginContour(tess)
        for point in polygon:
            gluTessVertex(tess, point, point)
        gluTessEndContour(tess)
    gluTessEndPolygon(tess)
    gluDeleteTess(tess)
    return vertices


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

    glTranslatef(0.0, 0.0, -3.0)

    vertices = slicing()
    # Draw Cube (multiple quads)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    for v in vertices:
        glVertex3f(v[0], v[1], v[2])
    # for plane in PLANES:
    #     for vertex, coord in zip(plane, COORDS):
    #         glTexCoord2f(coord[0], coord[1])
    #         glNormal3f(vertex[0], vertex[1], vertex[2])
    #         glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    lighting(False)
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('Lab3')

    glutDisplayFunc(DrawGLScene)
    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
