from OpenGL.GL import *
from curs.constants import *
import numpy

W = 0.2
N = 8

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
        self.is_rotated = False
        self.rotation_times = 0
        self.change_direction_times = 0
        self.unit = 1
        self.update(self.unit)

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        if not self.is_rotated:
            if self.rotation_times == N or self.rotation_times == N * 2:
                self.change_direction()
            self.rotate(self.unit)
        else:
            self.update(self.unit)
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

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))

    def position(self, t=0):
        self.t = t

    def change_direction(self):
        self.change_direction_times += 1
        self.rotation_times = 1
        self.is_rotated = False
        self.unit += 1

    def rotate(self, unit):
        if unit == 1:
            self.rotateXY()
        if unit == 2:
            self.rotateYZ()
        if unit == 3:
            self.rotateXY2()

    def rotateXY(self, direction=1):
        x0 = V[5][0]
        y0 = V[5][1]
        for i in range(len(V)):
            if (i == 5 or i == 6):
                continue
            vertex = V[i]
            x = vertex[0]
            y = vertex[1]
            R = numpy.sqrt(pow(x - x0, 2) + pow(y - y0, 2))
            angle = numpy.arccos((x - x0) / R)
            new_angle = angle + self.t
            if new_angle >= numpy.pi:
                self.is_rotated = True
                break
            new_x = x0 + direction * R * numpy.cos(new_angle)
            new_y = y0 + R * numpy.sin(new_angle)
            vertex[0] = new_x
            vertex[1] = new_y

    def rotateXY2(self):
        x0 = V[8][0]
        y0 = V[8][1]
        for i in range(len(V)):
            if (i == 8 or i == 7):
                continue
            vertex = V[i]
            x = vertex[0]
            y = vertex[1]
            R = numpy.sqrt(pow(x - x0, 2) + pow(y - y0, 2))
            angle = numpy.arccos((x - x0) / R)
            new_angle = angle - self.t
            if new_angle <= 0:
                self.is_rotated = True
                break
            new_x = x0 + R * numpy.cos(new_angle)
            new_y = y0 + R * numpy.sin(new_angle)
            vertex[0] = new_x
            vertex[1] = new_y

    def rotateYZ(self):
        y0 = V[8][1]
        z0 = V[8][2]
        for i in range(len(V)):
            if (i == 5 or i == 8):
                continue
            vertex = V[i]
            y = vertex[1]
            z = vertex[2]
            R = numpy.sqrt(pow(y - y0, 2) + pow(z - z0, 2))
            angle = numpy.arccos((z0 - z) / R)
            new_angle = angle + self.t
            if new_angle >= numpy.pi:
                self.is_rotated = True
                break
            new_y = y0 + R * numpy.sin(new_angle)
            new_z = z0 - R * numpy.cos(new_angle)
            vertex[1] = new_y
            vertex[2] = new_z

    def update(self, unit):
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
            if unit == 1:
                v[0] -= W * 2 * self.rotation_times
            if unit == 2:
                v[0] -= W * 2 * (N - 1)
                v[2] += W * 2 * self.rotation_times
            if unit == 3:
                v[0] -= W * 2 * (N - 1) - W * 2 * self.rotation_times
                v[2] += W * 2 * (N - 1)

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
