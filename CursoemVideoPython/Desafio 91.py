'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

Ex.:
Valores sorteados:
    O jogador1 tirou 5
    O jogador2 tirou 2
    O jogador3 tirou 6
    O jogador4 tirou 1
Ranking dos jogadores:
    1º lugar: jogador3 com 6
    2º lugar: jogador1 com 5
    3º lugar: jogador2 com 2
    4º lugar: jogador4 com 1
'''

from random import randint

jogador1 = randint(0, 9)
jogador2 = randint(0, 9)
jogador3 = randint(0, 9)
jogador4 = randint(0, 9)

jogadores = {'jogador1': jogador1,
             'jogador2': jogador2,
             'jogador3': jogador3,
             'jogador4': jogador4}

for i in range(4):

    if i == 0:
        maior = jogadores['jogador1']
    else:
        for j in range(i):
            if maior == 