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
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  
#se parte 0, ordena em relação às chaves
#Se for parte 1, ordena em relação aos valores
#Mas ordena em ordem crescente
#Para ordem descrecente, reverse=True

print('-='*30)
print('  == RANKING DO JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)