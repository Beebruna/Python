'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

totalGasto = contProd = i = 0
while True:
    print('\033[34m*\033[m' * 75)
    nomeProduto = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto: R$ '))

    while preco < 0:
        print('\033[31mEntrada Inválida! Tente Novamente!\033[m')
        preco = float(input('Digite o preço do produto: R$ '))

    i += 1
    totalGasto += preco

    if preco > 1000.0:
        contProd += 1

    if i == 1 or menor > preco:
        menor = preco
        nomeBarato = nomeProduto

    print('\033[34m*\033[m' * 75)
    continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip()[0]

    while continuar not in 'SsNn':
        print('\033[31mEntrada Inválida! Tente Novamente!')
        continuar = str(input('\033[33mDeseja Continuar? [S/N] ')).strip()[0]

    if continuar in 'Nn':
        break

print('\033[34m*'*75)
print(f'\033[35mO total gasto é R${totalGasto:.2f}')

if contProd == 0:
    print('\033[35mNão há produtos que custam mais de R$ 1.000,00')
elif contProd == 1:
    print('\033[35m1 produto custa mais de R$ 1.000,00')
else:
    print(f'\033[35m{contProd} produtos custam mais de R$ 1.000,00')

print(f'\033[35m{nomeBarato} é o produto mais barato e custa R$ {menor:.2f}')
print('\033[34m*'*75)
