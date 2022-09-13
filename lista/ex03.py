from pymprog import *

# Dados de entrada
E = [1100, 1800]  # disponibilidade de bebida
D = [960, 510, 895]  # demanda
C = [
    [3.7, 4.3, 6.1],
    [9.8, 6.9, 2.1]
]  # custos de envio

n = len(E)  # número de fábricas
m = len(D)  # número de clientes

# Modelo
begin('Transporte de bebidas')

# Variáveis de Decisão
A = iprod(range(n), range(m))  # Cria os indicies das variaveis x
x = var('x', A, int)  # Cria variável x com 2 indicies

# minimize(
#     sum(
#         sum(
#             C[i][j] * x[i][j] for j in range(m)
#         )
#         for i in range(n)
#     )
# ) MANEIRA DE FAZER

minimize(
    sum(
        C[i][j] * x[i, j] for i, j in A
    )
)

# Restrições

for j in range(m):
    sum(
        x[i, j] for i in range(n)
    ) == D[j]

for i in range(n):
    sum(
        x[i, j] for j in range(m)
    ) <= E[i]

# Resolver
solve()

# Valor otimo
print("Valor ótimo = {}".format(vobj()))

# Solução Otima
for i, j in A:
    print("x[{},{}] = {}".format(i+1, j+1, x[i, j].primal))

end()
