from pymprog import *

# leitura dos dados


def le_dados(inst):
    with open(inst, "r") as dados:
        capacidade = int(dados.readline())
        num_itens = int(dados.readline())
        peso = []
        valor = []
        quantidade = []
        cont = 0
        while cont < num_itens:
            aux = next(dados).split()
            peso.append(int(aux[0]))
            valor.append(int(aux[1]))
            quantidade.append(int(aux[2]))
            cont += 1

        separados = []
        for linha in dados:
            separados.append([int(linha.split()[0]), int(linha.split()[1])])

        return capacidade, num_itens, peso, valor, quantidade, separados

# função para o modelo do item


def mochila_a(caminho, instancia):
    capacidade, n, peso, valor, quantidade, separados = le_dados(
        caminho + instancia)

    begin("mochila")
    x = var("x", n, int)  # variável xi (quantidade carregada do item i)

    maximize(sum(valor[i] * x[i] for i in range(n)))

    sum(peso[i] * x[i] for i in range(n)) <= capacidade

    for i in range(n):
        x[i] <= quantidade[i]

    solve()

    print("{:20s}: {:10}".format(instancia, round(vobj())), end=" ")
    for i in range(n):
        if round(x[i].primal) != 0:
            print("  ({}, {}) ".format(i+1, round(x[i].primal)), end=" ")

    print()

# Instancias = ["inst_20_50.txt",
#               "inst_20_200.txt",
#               "inst_50_50.txt",
#               "inst_50_200.txt",
#               "inst_200_50.txt",
#               "inst_200_200.txt",
#               "inst_1000_50.txt",
#               "inst_1000_200.txt"]


Instancias = ["inst_20_50.txt"]

caminho = "./data/"

print("Mochila a)")
for inst in Instancias:
    mochila_a(caminho, inst)
