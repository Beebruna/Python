'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

* o aproveitamento será uma lista, onde tem os gols para cada jogo jogado.

ver imagem 9
'''

dict = {'nome': str(input('Nome do jogador: '))}
list = []
total = 0

qtdPartida = int(input(f'Quantas partidas {dict["nome"]} jogou? '))
 
for i in range(qtdPartida):
    list.append(int(input(f'Quantos gols na partida {i}? ')))
    total += list[i]

dict['gols'] = list[:]
dict['total'] = total
#ou dict['total'] = sum(list)

print('-='*30)
print(dict)
print('-='*30)
for k, v in dict.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)
print(f'O jogador {dict["nome"]} jogou {qtdPartida} partidas.')

for i, v in enumerate(list):
    print(f'     => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {total} gols.')



