'''
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print('O computador está pensando em um número entre 0 e 5...')
numComp = randint(0, 5)
sleep(3)
numUs = int(input("Adivinhe o número que o computador pensou: "))

if numUs == numComp:
    print('Você ACERTOU!')
else:
    print('Você ERROU!')
    print(f'O número pensado foi {numComp}.')


