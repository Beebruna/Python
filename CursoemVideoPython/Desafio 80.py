'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista = []

for i in range(5):
    num = int(input('Digite um número: '))

    if i == 0:
        maior = num
        lista.append(maior)
        print('Adicionado ao final da lista...')
    else:
        if maior < num:
            maior = num
            lista.append(maior)
            print('Adicionado ao final da lista...')
        else:
            if i > 1:
                pos = 0
                for j in range(len(lista) - 1):
                    if num >= lista[j]:
                        pos = j+1
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
            else:
                lista.insert(0, num)
                print('Adicionado na posição 0 da lista...')

print(f'Os valores digitados em ordem foram: {lista}')

'''
#Correção
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
'''