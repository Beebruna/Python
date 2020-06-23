'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final,
mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

print('\033[m\033[35m*\033[m' * 35)
print(' '*8 + 'CADASTRE UMA PESSOA' + ' '*8)
cont18 = cont20 = contHom = contMul = 0
while True:
    print('\033[m\033[35m*\033[m' * 35)
    idade = int(input('\033[mDigite a idade: '))

    while idade < 0 or idade > 110:
        print('\033[31mEntrada INVÁLIDA! Tente Novamente!\033[m')
        idade = int(input('Digite a idade: '))

    sexo = str(input('Digite o sexo: ')).strip()[0]

    while sexo not in 'FfMm':
        print('\033[31mEntrada INVÁLIDA! Tente Novamente!\033[m')
        sexo = str(input('Digite o sexo: ')).strip()[0]

    if idade >= 18:
        cont18 += 1

    if sexo in 'Mm':
        contHom += 1
    else:
        contMul += 1

        if idade < 20:
            cont20 += 1

    print('\033[35m*\033[m' * 35)
    continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip().upper()[0]

    while continuar not in 'SN':
        print('\033[31mEntrada INVÁLIDA! Tente Novamente!\033[m')
        continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print('\033[m\033[35m*\033[m'*55)

if cont18 == 0:
    print('\033[34mNão há pessoas maiores de 18 anos de idade cadastradas.')
elif cont18 == 1:
    print(f'\033[34mHá 1 pessoa maior de 18 anos de idade.')
else:
    print(f'\033[34mHá {cont18} pessoas maiores de 18 anos de idade.')

if contHom == 0:
    print('\033[34mNão há homens cadastrados.')
elif contHom == 1:
    print(f'\033[34mHá 1 homem cadastrado.')
else:
    print(f'Há {contHom} homens cadastrados.')

if contMul == 0:
    print('\033[34mNão há mulheres cadastradas.')
elif cont20 == 1:
    print(f'\033[34mHá 1 mulher com menos de 20 anos de idade cadastrada.')
else:
    print(f'\033[34mHá {cont20} mulheres menores de 20 anos de idade.\033[m')

print('\033[35m*\033[m'*55)