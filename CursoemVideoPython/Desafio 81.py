'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados;
B) A lista de valores, ordenados de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    print('*********************************')
    parada = str(input('Deseja continuar? [S/N] ')).strip()
    print('*********************************')

    while parada not in 'SsNn':
        print('Opção inválida! Digite novamente!')
        parada = str(input('Deseja continuar? [S/N] ')).strip()
        print('*********************************')

    if parada in 'Nn':
        print('Até mais!')
        break

print(f'\nTotal de números digitados: {len(lista)}')

lista.sort(reverse=True)

print(f'Lista em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
