from pymprog import *

D = [
    [900, 1500, 1300],
    [700, 900, 800]
]

C = [
    [1.5, 1.5, 2],
    [0.5, 0.5, 0.8]
]

CE = [
    [0.5, 0.25, 0],
    [0.25, 0.25, 0]
]

CP = [
    [200, 400, 400],
    [400, 500, 500]
]

T = [10, 8]

TL = [12, 8]

TD = [250, 320, 200]


n = len(T)
m = len(TD)

begin('cachaça')

A = iprod(range(n), range(m))
X = var('x', A)
J = var('j', m)
S = var('s', A, bool)
Y = var('y', range(-1, A))

minimize(sum(  # função objetiva

    (C[i][j] * X[i, j]) + (CE[i][j] * X[i, j]) + (CP[i][j] * S[i, j]) for i, j in A


))
