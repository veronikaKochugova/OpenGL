from OpenGL.GL import *
from curs.constants import *
import numpy

W = 0.2

V = [[-W, +W, +W],  # 0
     [-W, +W, -W],  # 1
     [+W, +W, -W],  # 2
     [+W, +W, +W],  # 3
     [0, 0, 0],  # 4
     [-W, -W, +W],  # 5
     [-W, -W, -W],  # 6
     [+W, -W, -W],  # 7
     [+W, -W, +W]]  # 8

T_PLANES = [
    (V[0], V[1], V[4]),
    (V[1], V[6], V[4]),
    (V[6], V[5], V[4]),
    (V[5], V[0], V[4]),
    #
    (V[3], V[2], V[4]),
    (V[2], V[7], V[4]),
    (V[7], V[8], V[4]),
    (V[8], V[3], V[4]),
    #
    #
    (V[0], V[1], V[4]),
    (V[1], V[2], V[4]),
    (V[2], V[3], V[4]),
    (V[3], V[0], V[4]),
    #
    (V[7], V[8], V[4]),
    (V[6], V[7], V[4]),
    (V[5], V[6], V[4]),
    (V[8], V[5], V[4])
]

Q_PLANES = [
    (V[0], V[3], V[8], V[5]),  # 1
    (V[0], V[1], V[6], V[5]),  # 2
    (V[1], V[2], V[7], V[6]),  # 3
    (V[2], V[3], V[8], V[7]),  # 4
]


class NotConvex:

    def __init__(self):
        self.t = 0.0
        self.direction = 0
        self.pos = 0
        self.is_rotated = False
        self.rotation_times = 0
        self.update()

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        # glTranslatef(-self.pos, 1, 0, 0)
        # glRotatef(self.direction, 0, 1, 0)
        if not self.is_rotated:
            self.rotate()
        else:
            self.update()
        # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glBegin(GL_TRIANGLES)
        for plane in T_PLANES:
            for vertex in plane:
                glNormal3f(vertex[0], vertex[1], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()

        # glBegin(GL_QUADS)
        # for plane in Q_PLANES:
        #     for vertex in plane:
        #         print(vertex)
        #         glNormal3f(vertex[0], vertex[1], vertex[2])
        #         glVertex3f(vertex[0], vertex[1], vertex[2])
        # glEnd()
        # glTranslatef(self.pos, 1, 0, 0)
        # glRotatef(-self.direction, 0, 1, 0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))

    def position(self, t=0):
        self.t = t

    def change_direction(self):
        # self.pos = 2 * W * self.rotation_times
        self.rotation_times = 1
        self.direction += 90
        self.is_rotated = True

    def rotate(self):
        x0 = V[5][0]
        y0 = V[5][1]
        print("=======================")
        for i in range(len(V)):
            if (i == 5 or i == 6):
                continue
            vertex = V[i]
            x = vertex[0]
            y = vertex[1]
            R = numpy.sqrt(pow(x - x0, 2) + pow(y - y0, 2))
            angle = numpy.arccos((x - x0) / R)
            # print(R)
            new_angle = angle + self.t
            print(new_angle)
            if new_angle >= numpy.pi:
                self.is_rotated = True
                break
            new_x = x0 + R * numpy.cos(new_angle)
            new_y = y0 + R * numpy.sin(new_angle)
            vertex[0] = new_x
            vertex[1] = new_y

    def update(self):
        global V
        global T_PLANES
        V = [[-W, +W, +W],  # 0
             [-W, +W, -W],  # 1
             [+W, +W, -W],  # 2
             [+W, +W, +W],  # 3
             [0, 0, 0],  # 4
             [-W, -W, +W],  # 5
             [-W, -W, -W],  # 6
             [+W, -W, -W],  # 7
             [+W, -W, +W]]  # 8
        for v in V:
            v[0] -= W * 2 * self.rotation_times
        T_PLANES = [
            (V[0], V[1], V[4]),
            (V[1], V[6], V[4]),
            (V[6], V[5], V[4]),
            (V[5], V[0], V[4]),
            #
            (V[3], V[2], V[4]),
            (V[2], V[7], V[4]),
            (V[7], V[8], V[4]),
            (V[8], V[3], V[4]),
            #
            #
            (V[0], V[1], V[4]),
            (V[1], V[2], V[4]),
            (V[2], V[3], V[4]),
            (V[3], V[0], V[4]),
            #
            (V[7], V[8], V[4]),
            (V[6], V[7], V[4]),
            (V[5], V[6], V[4]),
            (V[8], V[5], V[4])
        ]
        self.is_rotated = False
        self.rotation_times += 1
