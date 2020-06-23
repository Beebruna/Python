'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.
'''

'''
#1 a 60 sem repetições num mesmo jogo

from random import randint

jogador = []
jogo = []

qtd = int(input('Quantos jogos deseja fazer? '))

i = j = 0
while j < qtd:
    while i < 6:
        num = randint(1, 60)

        if num not in jogo:
            jogo.append(num)
        else:
            i -= 1
        i += 1
    jogador.append(jogo[:])
    jogo.clear()
    i = 0
    j += 1

print(f'\nQuantidade de jogos: {qtd}')
for i, jogo in enumerate(jogador):
    print(f'Jogo {i+1}: {jogo}')
'''

#Solução
from random import randint
from time import sleep

lista = list()
jogos = list()

print('=' * 30)
print('       JOGA NA MEGA SENA      ')
print('=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0

while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)

        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
