'''
Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.
'''

from random import randint
from time import sleep

print('\033[7;30m-'*44 + '\033[m')
print('\033[1m\033[7;30m' + ' '*9 + 'Vamos Jogar Par ou Ímpar.' + ' '*10 + '\033[m')
print('\033[7;30m-'*44 + '\033[m')

cont = 0
while True:

    palpiteJogador = str(input('Qual o seu palpite, ímpar [I] ou par [P]? ')).strip().upper()[0]

    while palpiteJogador not in 'IP':
        print('\033[31mOpção INVÁLIDA! Tente novamente!\033[m')
        palpiteJogador = str(input('Qual o seu palpite, ímpar [I] ou par [P]? ')).strip().upper()[0]

    valorJogador = int(input('Jogue um número entre 0 e 10: '))

    while valorJogador < 0 or valorJogador > 10:
        print('\033[31mOpção INVÁLIDA! Tente novamente!\033[m')
        valorJogador = int(input('Jogue um número entre 0 e 10: '))

    print('\nMinha Vez...')
    sleep(2)

    valorComputador = randint(0, 10)

    if palpiteJogador == 'P':
        palpiteComputador = 'I'
        print(f'Meu número é {valorComputador} e meu palpite é ÍMPAR.')
    else:
        palpiteComputador = 'P'
        print(f'Meu número é {valorComputador} e meu palpite é PAR.')

    resultado = (valorJogador + valorComputador) % 2

    sleep(1)

    print('=' * 44)
    print(f'Meu Jogo: \033[36mNúmero = {valorComputador}\033[m e \033[36mPalpite = {palpiteComputador}\033[m')
    print(f'Seu Jogo: \033[36mNúmero = {valorJogador}\033[m e \033[36mPalpite = {palpiteJogador}\033[m')
    print('=' * 44)

    if resultado == 0:
        if palpiteJogador == 'P':
            print(f'''\033[33mVocê GANHOU!
{valorJogador} + {valorComputador} = {valorJogador + valorComputador} que é PAR!\033[m''')
            print('=' * 44)
            cont += 1
        else:
            print(f'''\033[31mVocê PERDEU!
{valorJogador} + {valorComputador} = {valorJogador + valorComputador} que é PAR!\033[m''')
            print('=' * 44)
            break
    else:
        if palpiteJogador == 'I':
            print(f'''\033[33mVocê GANHOU!
{valorJogador} + {valorComputador} = {valorJogador + valorComputador} que é ÍMPAR!\033[m''')
            print('=' * 44)
            cont += 1
        else:
            print(f'''\033[31mVocê PERDEU!
{valorJogador} + {valorComputador} = {valorJogador + valorComputador} que é ÍMPAR!\033[m''')
            print('=' * 44)
            break

if cont == 0:
    print('\033[1m\033[7;34mVocê não venceu em nenhuma vez...\033[m')
elif cont > 1:
    print(f'\033[1m\033[7;34mVocê venceu em {cont} vitórias!\033[m')
else:
    print(f'\033[1m\033[7;34mVocê venceu em uma única vitória!\033[m')
print('=' * 44)

