# Importando biblioteca Numpy
import numpy as np

# Dados de entrada ligas metálicas
A = np.matrix([[0.5, 0.3, 1, 0, 0],
               [0.1, 0.2, 0, 1, 0],
               [0.4, 0.5, 0, 0, 1]])

b = np.matrix([[3],
               [1],
               [3]])

c = np.matrix([[-3],
               [-2],
               [0],
               [0],
               [0]])

base = [2, 3, 4]

# Matriz B
B = np.matrix(A[:, base])
print("B =")
print(B)

print()

# Solução básica
xB = np.linalg.inv(B) * b
print("xB =")
print(xB)

# Vetor pT
pT = c[base].T * np.linalg.inv(B)
print("pT = ", pT)

# Custos relativos
s = c.T - pT * A
print("s = ", s)

# Verifica se a solução é ótima
mins = s.min()  # Calcula o valor mínimo de s
p1 = s.argmin()  # Retorna a posição do valor mínimo no vetor s
print("mins = ", mins)
print("p1 = ", p1)

# Vetor auxiliar y
y = np.linalg.inv(B) * A[:, p1]
print("y =")
print(y)
print()

# Teste da razão
r = xB / y
print("r =")
print(r)
print()

# Eliminando valores negativos do vetor r
r[r < 0] = np.inf
print("r =")
print(r)

# Determina variável que sai da base
minr = r.min()
p2 = r.argmin()
print("minr = ", minr)
print("p2 = ", p2)

# Atualiza a base
base[p2] = p1
print(base)

# Solução ótima
x = np.zeros([c.size, 1])  # Cria matriz nula para escrever a solução
x[base] = xB  # Coloca os valores da solução básica nas posições corretas da matriz de solução
# print(x)
for i in range(c.size):
    print("x[{}] = {}".format(i+1, x[i, 0]))

# Valor ótimo
vo = (c.T * x)
print("Valor ótimo = ", vo)
