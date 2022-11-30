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


# função para o modelo do item b)
def mochila_b(caminho, instancia):
    capacidade, n, peso, valor, quantidade, separados = le_dados(
        caminho + instancia)
    M = 100000  # M grande

    begin("mochila")

    print("\n*****************************\nArquivo: {}\n".format(instancia))

    x = var("x", n, int)  # variável da quantidade carregada de cada item
    # variável s para identificar se um item foi ou não carregado
    s = var("s", n, bool)

    maximize(sum(valor[i] * x[i] for i in range(n)))

    sum(peso[i] * x[i] for i in range(n)) <= capacidade

    for i in range(n):
        x[i] <= quantidade[i] * s[i]

    for par in separados:
        s[par[0]-1] + s[par[1]-1] <= 1

    solve()

    print("\n\nValor ótimo -> {}".format(round(vobj())))
    for i in range(n):
        if round(x[i].primal) != 0:
            print("\n(Índice -> {}, Quantidade -> {}) ".format(i +
                  1, round(x[i].primal)))

    print()


Instancias = ["inst_20_50.txt",
              "inst_20_200.txt",
              "inst_50_50.txt",
              "inst_50_200.txt",
              "inst_200_50.txt",
              "inst_200_200.txt",
              "inst_1000_50.txt",
              "inst_1000_200.txt"]

caminho = "./data/"

print("Mochila b)")
for inst in Instancias:
    mochila_b(caminho, inst)
