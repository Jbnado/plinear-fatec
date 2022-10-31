from pymprog import *

# Parametros

BM = 4  # Quantidade de barcos que podem ser produzidos em um mes
BE = 3  # Quantidade de barcos que podem ser estocados em um mes
CB = 10000  # Custo fixo de construção de um barco
CP = 4000  # Custo de produção mensal fixo para construção de barcos
CE = 3000  # Custo para manter um barco em estoque por mês
D = [
    1, 2, 5, 3, 2, 6, 3, 2
]  # Demanda de barcos por mes

n = len(D)  # Quantidade de meses

# Variaveis

begin('Problemas dos Barcos')

X = var("x", n, int)  # Quantidade de barcos produzidos em um mes
Y = var('y', range(-1, n), int)  # Quantidade estocado no mes
S = var('s', n, bool)  # Se foi produzido ou nao naquele mes

# Funcao Objetivo

minimize(
    sum(
        (X[i] * CB) + (Y[i] * CE) + (S[i] * CP) for i in range(n)
    )
)

# Restricoes (s.a)

for i in range(n):
    X[i] + Y[i - 1] - Y[i] >= D[i]
    Y[i] <= BE
    X[i] <= BM
    X[i] >= 0
    Y[i] >= 0

Y[-1] == 0


# Resolvendo
solve()

print()
print("Valor ótimo = {}".format(vobj()))
print()

for i in range(n):
    print('Mes {} -> Produziu {} e estocou {}'.format(i +
          1, X[i].primal, Y[i].primal))

# Fim
end()
