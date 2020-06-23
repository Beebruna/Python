'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado.

No final,mostre a matriz na tela, com a formatação correta.
'''

'''
matriz = [[],[],[]]

j = 0
for i in range(1, 10):
    matriz[j].append(int(input(f'Digite o {i}º número: ')))

    if i % 3 == 0:
        j += 1

print('\nMatriz 3x3')
for i in range(3):
    print('|', end='')
    for j in range(3):
        if j < 2:
            print(f'{matriz[i][j]}', end=' ')
        else:
            print(f'{matriz[i][j]}', end='|')
    print()
'''

#Solução
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()