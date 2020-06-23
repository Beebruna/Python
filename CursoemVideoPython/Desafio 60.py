'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex.:
5! = 5x4x3x2x1 = 120
'''

n = int(input('Digite um número inteiro: '))

if n == 0:
    print(f'O fatorial de {n} é 1')
else:
    fat = 1
    i = n
    while i != 0:
        fat = fat * i
        i -= 1
    print(f'O fatorial de {n} é {fat}')

'''
#Correção 1
from math import factorial

n = int(input('Digite um número inteiro: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')
'''

'''
#Correção 2
n = int(input('Digite um número inteiro para calcular o seu Fatorial: '))

c = n
f = 1
print(f'Calculando {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')
'''