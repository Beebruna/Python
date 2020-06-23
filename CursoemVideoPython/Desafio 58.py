'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''

from random import randint
from time import sleep
'''
print('O computador está pensando em um número entre 0 e 10...')

numComp = randint(0, 10)
sleep(3)

numUs = int(input("Adivinhe o número que o computador pensou: "))

if numUs == numComp:
    print('\033[1;32mVocê \033[4mACERTOU\033[0;32m \033[1mna 1º tentativa!')
else:
    palpite = 1
    while numUs != numComp:
        print('\033[31mVocê errou!\nTente novamente')
        numUs = int(input("\033[35mAdivinhe o número que o computador pensou: "))
        palpite += 1
    print(f'\033[7;33mVocê acertou na {palpite}º tentativa!\033[m')
'''
#Correção
computador = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0
while not acertou:

    jogador =int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com {palpites} tentativas. Parabéns!')





