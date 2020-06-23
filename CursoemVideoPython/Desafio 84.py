'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

'''
nome = list()
peso = list()

while True:
    nome.append(str(input('Digite o nome: ')))
    peso.append(float(input('Digite o peso: ')))

    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()

    while continuar not in 'sn':
        print('Opção inválida! tente novamente')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()

    if continuar in 'n':
        print('Até mais!')
        break

if len(nome) > 1:
    print(f'\nForam cadastradas {len(nome)} pessoas')
elif len(nome) == 1:
    print(f'\nFoi cadastrada apenas 1 pessoa.')
else:
    print(f'\nNão há pessoas cadastradas!')

maior = max(peso)
print(f'\nPessoas mais pesadas com {maior:.2f}kg: ', end='')

for i in range(len(peso)):
    if maior == peso[i]:
        print(f'{nome[i].capitalize()}', end=' ...')

menor = min(peso)
print(f'\nPessoas mais leves com {menor:.2f}kg: ', end='')

for i in range(len(peso)):
    if menor == peso[i]:
        print(f'{nome[i].capitalize()}', end=' ...')
'''

#Correção
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]

        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')

print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
