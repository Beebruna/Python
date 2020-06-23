'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência  de Fibonacci.

Ex.:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
'''
n = int(input('Digite um número: '))

print(f'Sequência de Fibonacci de {n} termos')

i = 0
a2 = 1
an = 0
soma = 0
while i < n:
    if i == 0:
        print('0', end='')
    if i == 1:
        print(' -> 1', end='')
    if i > 1:
        if soma < 2:
            soma = soma + a2
            an = soma

            if soma == 1:
                print(end=' -> ')
        else:
            soma = an + a2
            a2 = an
            an = soma
        if i < n-1:
            print(f'{soma}', end=' -> ')
        else:
            print(f'{soma}')
    i += 1
'''
#Correção
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)

