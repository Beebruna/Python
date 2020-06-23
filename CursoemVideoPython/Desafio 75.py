'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
'''
a0 = int(input('Digite um número: '))
a1 = int(input('Digite um número: '))
a2 = int(input('Digite um número: '))
a3 = int(input('Digite um número: '))

tupla = (a0, a1, a2, a3)

nove = tupla.count(9)

if nove == 0:
    print('O número 9 não existe!')
elif nove == 1:
    print(f'O número 9 apareceu {tupla.count(9)} vez')
else:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')

for i in range(4):
    if tupla[i] == 3:
        pos = i
        break
    else:
        pos = 0

if pos == 0:
    print(f'O valor 3 não existe em nenhuma posição!')
else:
    print(f'A primeira ocorrência do número 3 foi na posição {pos}')

print(f'Números pares inseridos: ', end='')
if a0 % 2 == 0:
    print(a0, end=' ')
if a1 % 2 == 0:
    print(a1, end=' ')
if a2 % 2 == 0:
    print(a2, end=' ')
if a3 % 2 == 0:
    print(a3)
'''
#Correção
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(f'O valor 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print(f'Os valores pares digitados foram ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')



