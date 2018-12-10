def surfaceXY(x, y, z, n=6):
    V = []
    dx = x / n
    dy = y / n
    N = n + 1  # N - number of points
    x0 = -x / 2
    y0 = -y / 2
    for i in range(N):
        for j in range(N):
            v = [x0 + i * dx, y0 + j * dy, z]
            V.append(v)
    P = []
    for i in range(n):
        for j in range(n):
            p = [V[N * i + j], V[N * i + j + 1], V[N * (i + 1) + j + 1], V[N * (i + 1) + j]]
            P.append(p)
    return P


def surfaceYZ(x, y, z, n=6):
    V = []
    dz = z / n
    dy = y / n
    z0 = -z / 2
    y0 = -y / 2
    N = n + 1  # N - number of points
    for j in range(N):
        for i in range(N):
            v = [x, y0 + i * dy, z0 + j * dz]
            V.append(v)
    P = []
    for i in range(n):
        for j in range(n):
            p = [V[N * i + j], V[N * i + j + 1], V[N * (i + 1) + j + 1], V[N * (i + 1) + j]]
            P.append(p)
    return P


def surfaceXZ(x, y, z, n=6):
    V = []
    dz = z / n
    dx = x / n
    x0 = -x / 2
    z0 = -z / 2
    N = n + 1  # N - number of points
    for j in range(N):
        for i in range(N):
            v = [x0 + dx * i, y, z0 + j * dz]
            V.append(v)
    P = []
    for i in range(n):
        for j in range(n):
            p = [V[N * i + j], V[N * i + j + 1], V[N * (i + 1) + j + 1], V[N * (i + 1) + j]]
            P.append(p)
    return P
