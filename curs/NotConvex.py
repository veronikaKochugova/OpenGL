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
        self.is_rotated = False
        self.rotation_times = 0
        self.change_direction_times = 0
        self.direction_is_changed = False
        self.update(self.direction_is_changed)

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        if not self.is_rotated:
            if self.rotation_times > 4:
                self.change_direction()
            self.rotate(self.direction_is_changed)
        else:
            self.update(self.direction_is_changed)
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
        self.direction_is_changed = True

    def rotate(self, flag=True):
        if not flag:
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
                new_x = x0 + R * numpy.cos(new_angle)
                new_y = y0 + R * numpy.sin(new_angle)
                vertex[0] = new_x
                vertex[1] = new_y
        else:
            self.rotateYZ()

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
            if i == 0:
                print(angle)
            new_angle = angle + self.t
            if i == 0:
                print(new_angle)
            if new_angle >= numpy.pi:
                self.is_rotated = True
                break
            new_y = y0 + R * numpy.sin(new_angle)
            new_z = z0 - R * numpy.cos(new_angle)
            vertex[1] = new_y
            vertex[2] = new_z

    def update(self, flag):
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
            if not flag:
                v[0] -= W * 2 * self.rotation_times
            else:
                v[0] -= W * 2 * 4
                v[2] += W * 2 * self.rotation_times

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
