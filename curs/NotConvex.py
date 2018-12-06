from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
from curs.constants import *
import numpy

CUBE_WIDTH = 0.2

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


class NotConvex:

    def __init__(self, width=CUBE_WIDTH):
        self.w = width
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        position = (0.0, 0.0, 1.0)
        glTranslatef(*position)

        glTranslatef(self.x * 0.1, 0.0, 0.0)
        glRotatef(60 * self.x, 0.0, 0.0, 1)

        glBegin(GL_QUADS)
        for plane in PLANES:
            for vertex, coord in zip(plane, COORDS):
                glTexCoord2f(coord[0], coord[1])
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()

        # undo changes
        glTranslatef(-position[0], -position[1], -position[2])
        glRotatef(60 * self.x, 0.0, 0.0, -1)
        glTranslatef(-self.x * 0.1, 0.0, 0.0)

    def position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
