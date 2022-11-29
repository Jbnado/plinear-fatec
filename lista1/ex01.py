from pymprog import *

P = [10, 25, 20]  # preço de venda
C = [6, 15, 14]  # custo de produção
L = [1000, 0, 100]  # produção minima
U = [6000, 500, 1000]  # producao maxima
D = [400, 400, 500, 2000]  # disponibilidade de recurso
Q = [
    [0.03, 0.15, 0.1],
    [0.06, 0.12, 0.1],
    [0.05, 0.1, 0.12],
    [0, 2, 1.2]
]

n = len(P)  # qntd de produtos
m = len(D)  # qntd de recursos

# -> Modelo

begin('Utensilios de Metal')

# -> Variaveis de Decisão

x = var("x", n, int)  # cria n variáveis inteiras não negativas

# -> Função Objetivo
maximize(
    sum(
        (P[i] - C[i]) * x[i] for i in range(n)
    )
)

# -> Restrições

for j in range(m):
    sum(
        Q[j][i] * x[i] for i in range(n)
    ) <= D[j]

for i in range(n):
    L[i] <= x[i] <= U[i]

# Resolver
solve()

# Valor otimo
print("Valor ótimo = {}".format(vobj()))

# Solução Otima
for i in range(n):
    print("x[{}] = {}".format(i+1, x[i].primal))

end()
