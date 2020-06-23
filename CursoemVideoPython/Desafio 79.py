'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = list()

while True:
    num = int(input(('Digite um número: ')))

    if num in lista:
        print('Esse valor já existe e não será adicionado!')
    else:
        lista.append(num)
        print('Número adicionado com Sucesso!')

    print('-------------------------------------------')
    parada = str(input('Deseja continuar inserindo números? [S/N] ')).strip()
    print('-------------------------------------------')

    while parada not in 'NnSs':
        print('Opção Inválida! Digite novamente!')
        parada = str(input('Deseja continuar inserindo números? [S/N] ')).strip()
        print('-------------------------------------------')

    if parada in 'Nn':
        print('Até mais!')
        break

lista.sort()
print(f'\nValores digitados em ordem crescente: {lista}')