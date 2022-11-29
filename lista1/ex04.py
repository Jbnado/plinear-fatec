from pymprog import *

# Dados de entrada
P = [80, 90]  # Capacidade produtiva

D = [50, 40, 65]  # Demanda dos Clientes

CFP = [
    [10, 12, 20],
    [15, 8, 11]
]  # Custo fazendas p/ centro de processamentos

CPC = [
    [7, 7, 20],
    [8, 9, 10],
    [24, 8, 6]
]

n = len(P)
m = len(CPC)
l = len(D)

begin('Minimizar Envio de Carnes')

# Variaveis de decisao
A = iprod(range(n), range(m))
x = var('x', A)

B = iprod(range(m), range(l))
y = var('y', B)

minimize(
    sum(
        CFP[i][j] * x[i, j] for i, j in A
    )
    +
    sum(
        CPC[j][k] * y[j, k] for j, k in B
    )
)

for k in range(l):
    sum(
        y[j, k] for j in range(m)
    ) == D[k]

for i in range(n):
    sum(
        x[i, j] for j in range(m)
    ) <= P[i]

for j in range(m):
    sum(
        x[i, j] for i in range(n)
    ) == sum(
        y[j, k] for k in range(l)
    )

# Resolver
solve()

# Valor otimo
print("Valor ótimo = {}".format(vobj()))

print()

# Solução Otima
for i, j in A:
    print("x[{},{}] = {}".format(i+1, j+1, x[i, j].primal))

print()

for j, k in B:
    print("y[{},{}] = {}".format(j+1, k+1, y[j, k].primal))

print()
end()
