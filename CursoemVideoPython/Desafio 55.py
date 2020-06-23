'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidos.
'''

'''
#Usando Lista
pesos = []

for i in range(5):
    pesos.append(float(input(f'Digite o peso da {i+1}ª pessoa: ')))

maior = pesos[0]
menor = pesos[0]

for i in range(4):
    if maior < pesos[i+1]:
        maior = pesos[i+1]

    if menor > pesos[i+1]:
        menor = pesos[i+1]

print(f'\nO maior peso vale {maior:.2f}kg')
print(f'O menor peso vale {menor:.2f}kg')
'''

'''
#Utilizando função
print(f'\nO maior peso vale {max(pesos):.2f}kg')
print(f'O menor peso vale {min(pesos):.2f}kg')
'''

for i in range(5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa: '))

    if i == 0:
    #ou coloco o primeiro peso fora do laço
        maior = menor = peso
    else:
        if maior < peso:
            maior = peso

        if menor > peso:
            menor = peso

print(f'\nO maior peso vale {maior:.2f}kg')
print(f'O menor peso vale {menor:.2f}kg')

