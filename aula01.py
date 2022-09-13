from pymprog import *

disponibilidadeMateria = [3, 1, 3]

receitaPorTon = [3, 2]

percentualMateriaPrima = [
    [0.5, 0.3],
    [0.1, 0.2],
    [0.4, 0.5]
]

quantidadeMaterias = len(disponibilidadeMateria)
quantidadeLigas = len(receitaPorTon)

begin('Ligas')
quantidadeProduzida = var('quantidadeProduzida_', quantidadeLigas)

maximize(sum(receitaPorTon[i] * quantidadeProduzida[i]
         for i in range(quantidadeLigas)))

for j in range(quantidadeMaterias):
    sum(
        percentualMateriaPrima[j][i] * quantidadeProduzida[i] for i in range(quantidadeLigas)
    ) <= disponibilidadeMateria[j]

solve()

print('Valor otimo = ', format(vobj()))

for i in range(quantidadeLigas):
    print('x[{:.2f}] = {:.2f}'.format(i+1, quantidadeProduzida[i].primal))

end()
