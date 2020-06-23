'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import choice
from time import sleep

print('Vamos jogar pedra, papel tesoura!')

print("""Escolha uma opção entre pedra, papel e tesoura!""")

print('\nPrepare-se...')
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(1)
print('Vai!')

jogador = str(input('Digite aqui: ')).strip().lower()

computador = choice(['pedra', 'papel', 'tesoura'])

if jogador == computador:
    print('Empate!')
elif jogador == 'pedra' and computador == 'papel':
    print('Papel cobre Pedra, EU GANHEI!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Pedra quebra tesoura, VOCÊ GANHOU!')
elif jogador == 'papel' and computador == 'pedra':
    print('Papel cobre Pedra, VOCÊ GANHOU!')
elif jogador == 'papel' and computador == 'tesoura':
    print('Tesoura corta papel, EU GANHEI!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Pedra quebra tesoura, EU GANHEI!')
elif jogador == 'tesoura' and computador == 'papel':
    print('Tesoura corta papel, VOCÊ GANHOU!')