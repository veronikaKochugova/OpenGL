from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
from curs.constants import *
import numpy

CUBE_WIDTH = 0.2
W = 0.2

# V = [[+CUBE_WIDTH, +CUBE_WIDTH, +CUBE_WIDTH],
#      [+CUBE_WIDTH, +CUBE_WIDTH, -CUBE_WIDTH],
#      [+CUBE_WIDTH, -CUBE_WIDTH, -CUBE_WIDTH],
#      [-CUBE_WIDTH, -CUBE_WIDTH, -CUBE_WIDTH],
#      [-CUBE_WIDTH, -CUBE_WIDTH, +CUBE_WIDTH],
#      [-CUBE_WIDTH, +CUBE_WIDTH, +CUBE_WIDTH],
#      [+CUBE_WIDTH, -CUBE_WIDTH, +CUBE_WIDTH],
#      [-CUBE_WIDTH, +CUBE_WIDTH, -CUBE_WIDTH]]
#
# PLANES = [
#     (V[2], V[3], V[7], V[1]),  # 1
#     (V[6], V[2], V[1], V[0]),  # 2
#     (V[4], V[6], V[0], V[5]),  # 3
#     (V[3], V[4], V[5], V[7]),  # 4
#     (V[6], V[4], V[3], V[2]),  # 5
#     (V[5], V[0], V[1], V[7]),  # 6
# ]
#
# COORDS = ([0, 0], [CUBE_WIDTH, 0], [CUBE_WIDTH, CUBE_WIDTH], [0, CUBE_WIDTH])

V = [[-W, +W, +W],  # 0
     [-W, +W, -W],  # 1
     [+W, +W, -W],  # 2
     [+W, +W, +W],  # 3
     [0, 0, 0],  # 4
     [-W, -W, +W],  # 5
     [-W, -W, -W],  # 6
     [+W, -W, -W],  # 7
     [+W, -W, +W]]  # 8

PLANES = [
    # (V[0], V[3], V[8], V[5]),  # 1
    # (V[0], V[1], V[6], V[5]),  # 2
    # (V[1], V[2], V[7], V[6]),  # 3
    # (V[2], V[3], V[8], V[7]),  # 4
    #
    (V[0], V[1], V[4]),  # 5
    (V[0], V[3], V[4]),  # 6
    (V[3], V[2], V[4]),  # 7
    (V[1], V[2], V[4]),  # 8
    #
    (V[7], V[8], V[4]),  # 9
    (V[6], V[7], V[4]),  # 10
    (V[5], V[6], V[4]),  # 11
    (V[8], V[5], V[4])  # 12
]


class NotConvex:

    def __init__(self, width=CUBE_WIDTH):
        self.w = width
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.t = 0.0

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, WHITE_L)

        glTranslatef(0, -CUBE_WIDTH, 0)
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.t, 0, 1, 0)
        glRotatef(-(self.t * 1.3), 0, 0, 1)

        glBegin(GL_QUADS)
        for plane in PLANES:
            for vertex in plane:
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()

        # undo changes
        glTranslatef(-self.x, -self.y, -self.z)
        glRotatef((self.t * 1.3), 0, 0, 1)
        glRotatef(-self.t, 0, 1, 0)
        glTranslatef(0, -CUBE_WIDTH, 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))
        # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))

    def position(self, x, y, z, t=0):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
