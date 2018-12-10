def surfaceXY(x, y, z, n=6):
    V = []
    dx = x / n
    dy = y / n
    N = n + 1  # N - number of points
    for i in range(N):
        for j in range(N):
            v = [i * dx, j * dy, z]
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
    N = n + 1  # N - number of points
    for j in range(N):
        for i in range(N):
            v = [x, i * dy, j * dz]
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
    N = n + 1  # N - number of points
    for j in range(N):
        for i in range(N):
            v = [dx * i, y, j * dz]
            V.append(v)
    P = []
    for i in range(n):
        for j in range(n):
            p = [V[N * i + j], V[N * i + j + 1], V[N * (i + 1) + j + 1], V[N * (i + 1) + j]]
            P.append(p)
    return P
