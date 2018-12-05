from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy

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


class Cube:

    def __init__(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

        # initialize texture mapping
        glEnable(GL_TEXTURE_2D)
        self.load_texture()

    def draw(self):
        glTranslatef(0.0, 0.0, -6.0)
        # Draw Cube (multiple quads)
        glBegin(GL_QUADS)
        for plane in PLANES:
            for vertex, coord in zip(plane, COORDS):
                glTexCoord2f(coord[0], coord[1])
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()
        glTranslatef(0.0, 0.0, 6.0)

    def load_texture(self):
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
