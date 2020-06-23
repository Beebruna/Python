'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
listaP = []
listaI = []

while True:
    lista.append(int(input('Digite um número: ')))

    print('*********************************')
    parada = str(input('Deseja continuar? [S/N] ')).strip()
    print('*********************************')

    while parada not in 'SsNn':
        print('Opção inválida! Digite Novamente!')
        parada = str(input('Deseja continuar? [S/N] ')).strip()
        print('*********************************')

    if parada in 'Nn':
        print('Até Mais!\n')
        break

for i in lista:
    if i%2 == 0:
        listaP.append(i)
    else:
        listaI.append(i)

print(f'Lista principal: {lista}')
print(f'Lista de números pares: {listaP}')
print(f'Lista de números ímpares: {listaI}')

