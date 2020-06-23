'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
'''

from random import randint

'''
a0 = randint(0, 10)
a1 = randint(0, 10)
a2 = randint(0, 10)
a3 = randint(0, 10)
a4 = randint(0, 10)

tupla = (a0, a1, a2, a3, a4)

if a0 >= a1 and a0 >= a2 and a0 >= a3 and a0 >= a4:
    maior = a0
elif a1 >= a0 and a1 >= a2 and a1 >= a3 and a1 >= a4:
    maior = a1
elif a2 >= a0 and a2 >= a1 and a2 >= a3 and a0 >= a4:
    maior = a2
elif a3 >= a0 and a3 >= a1 and a3 >= a2 and a3 >= a4:
    maior = a3
else:
    maior = a4

if a0 <= a1 and a0 <= a2 and a0 <= a3 and a0 <= a4:
    menor = a0
elif a1 <= a0 and a1 <= a2 and a1 <= a3 and a1 <= a4:
    menor = a1
elif a2 <= a0 and a2 <= a1 and a2 <= a3 and a0 <= a4:
    menor = a2
elif a3 <= a0 and a3 <= a1 and a3 <= a2 and a3 <= a4:
    menor = a3
else:
    menor = a4

print(f'Tupla: {tupla}')
print(f'Maior número da Tupla: {maior}')
print(f'Menor número da Tupla: {menor}')
'''

#Correção
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Valores Sorteados: {numeros}')
print(f'O maior valor sorteado é: {max(numeros)}')
print(f'O maior valor sorteado é: {min(numeros)}')
