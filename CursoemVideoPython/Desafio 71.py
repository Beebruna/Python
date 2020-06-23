'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.

OBS.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''
'''
print('\033[30m=' * 52)
print(
    'Notas existentes: \033[34mR$50,00\033[30m, \033[34mR$20,00\033[30m, \033[34mR$10,00\033[30m, \033[34mR$1,00\033[m')
print('\033[30m=\033[m' * 52)

while True:
    valor = int(input('Digite o valor a ser sacado: R$ '))

    while valor < 0:
        print('\033[31mValor Inválido! Digite Novamente!\033[m')
        valor = int(input('Digite o valor a ser sacado: '))

    print('\033[30m=\033[m' * 52)
    print(f'\033[35mValor do Saque: R${valor:.2f}')

    if valor == 0:
        print('\033[31mNão há valor para ser sacado!')
    else:
        if valor >= 50:
            ced50 = valor // 50
            resto50 = valor % 50

            if ced50 == 1:
                print(f'\033[35m{ced50} cédula de R$50,00')
            else:
                print(f'\033[35m{ced50} cédulas de R$50,00')
        else:
            resto50 = valor

        if resto50 >= 20:
            ced20 = resto50 // 20
            resto20 = resto50 % 20

            if ced20 == 1:
                print(f'\033[35m{ced20} cédula de R$20,00')
            else:
                print(f'\033[35m{ced20} cédulas de R$20,00')
        else:
            resto20 = resto50

        if resto20 >= 10:
            ced10 = resto20 // 10
            resto10 = resto20 % 10

            if ced10 == 1:
                print(f'\033[35m{ced10} cédula de R$10,00')
            else:
                print(f'\033[35m{ced10} cédulas de R$10,00')
        else:
            resto10 = resto20

        if resto10 >= 1:
            ced1 = resto10

            if ced1 == 1:
                print(f'\033[35m{ced1} cédula de R$1,00')
            else:
                print(f'\033[35m{ced1} cédulas de R$1,00')

    print('\033[36m*\033[m' * 52)
    continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip()[0]

    while continuar not in 'SsNn':
        print('\033[31mValor Inválido! Digite Novamente!')
        continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip()[0]

    if continuar in 'Nn':
        print('\033[36m*\033[m' * 52)
        print('\033[7;33mOperação Realizada com Sucesso!\033[m')
        break

    resto50 = resto20 = resto10 = resto1 = 0

    print('\033[36m*\033[m' * 52)
'''
# Correção
print('=' * 30)
print(' '*10 + 'BANCO CEV' + ' '*11)
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totCed = 0

while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totCed = 0

        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')