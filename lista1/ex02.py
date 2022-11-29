from pymprog import *

# -> PARAMETROS

C = [
    5.2, 6.8, 7.1, 2.5
]  # Custo de cada ingrediente
Rmax = [
    1, 1, 0.55, 0.08
]  # Maximo que pode se utilizar de cada ingrediente
Rmin = [
    0.22, 0.07, 0, 0
]  # Minimo que pode se utilizar de cada ingrediente
P = [
    [0.26, 0.01, 0.25, 0.1],
    [0.05, 0.05, 0.26, 0.02],
    [0.6, 0.75, 0.45, 0.24],
    [0.07, 0, 0.01, 0.01]
]  # Percentual de nutriente em cada ingrediente
n = len(C)  # n ingredientes
m = len(P)  # m nutrientes

# -> Modelo
begin('Minimizar custos de 1kg de barra de cereal')

# -> Variaveis de decisao
x = var('x', n)

# -> Funcao Objetivo
minimize(
    sum(C[i] * x[i] for i in range(n))
)

# -> Restricoes
for j in range(m):
    Rmax[j] >= sum(P[j][i] * x[i] for i in range(n)) >= Rmin[j]

sum(x[i] for i in range(n)) == 1

# Resolver
solve()

# Valor otimo
print()
print("Valor ótimo = {}".format(vobj()))
print()

# Solução Otima
for i in range(n):
    print("x[{}] = {}".format(i+1, x[i].primal))

end()
