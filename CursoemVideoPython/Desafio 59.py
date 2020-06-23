'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

opcao = 0

while opcao != 5:

    print("""O que deseja fazer?
    \033[33m[1]\033[m somar;
    \033[33m[2]\033[m multiplicar;
    \033[33m[3]\033[m maior;
    \033[33m[4]\033[m novos números;
    \033[33m[5]\033[m sair do programa;""")
    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('\033[36m=-\033[m' * 20)
        print(f'\033[34m{n1} + {n2} = {soma}\033[m')
    elif opcao == 2:
        produto = n1*n2
        print('\033[36m=-\033[m' * 20)
        print(f'\033[34m{n1} x {n2} = {produto}\033[m')
    elif opcao == 3:
        if n1 > n2:
            print('\033[36m=-\033[m' * 20)
            print(f'\033[34m{n1} é o maior valor!\033[m')
        else:
            print('\033[36m=-\033[m' * 20)
            print(f'\033[34m{n2} é o maior valor!\033[m')
    elif opcao == 4:
        print('\033[36m=-\033[m' * 20)
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
    elif opcao == 5:
        print('\033[36m=-\033[m'*20)
        print('\033[34mFinalizando...\033[m')
    else:
        print('\033[36m=-\033[m'*20)
        print('\033[1;31mOpção Inválida! Tente Novamente!\033[m')
    print('\033[36m=-\033[m'*20)
    sleep(2)
print('\033[7;35mAté mais!\033[m')