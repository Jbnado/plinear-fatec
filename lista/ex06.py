from pymprog import *

# Parametros
T = [
    54, 83, 15, 71, 77, 36, 53, 38, 27, 87, 76, 91, 14, 29, 12, 77, 32, 87, 68, 94, 79, 3, 11, 99, 56, 70, 99, 60, 5, 56, 3, 61, 73, 75, 47, 14, 21, 86, 5, 77, 16, 89
]  # Tempos de realização das tarefas
n = 6  # Operadores

m = len(T)


begin('tarefas e operadores')

A = iprod(range(n), range(m))
x = var('x', A, bool)

Z = var('z')

minimize(Z)

for j in range(m):
    sum(x[i, j] for i in range(n)) == 1

for i in range(n):
    sum(
        T[j] * x[i, j] for j in range(m)
    ) <= Z

solve()

# Valor otimo
print()
print("Valor ótimo = {}".format(vobj()))
print()

# Solução Otima
for i, j in A:
    print("x[{},{}] = {}".format(i+1, j+1, x[i, j].primal))

end()
