'''
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.
'''

n = int(input('Digite um número: '))

print('\nTabuada do número', n)
print('\nAdição' + ' '*31 + 'Subtração')
print(f'{n} + {1:2} = {n+1:2}' + ' '*24 + f'{n:2} - {n} = 0')
print(f'{n} + {2:2} = {n+2:2}' + ' '*24 + f'{n+1:2} - {n} = 1')
print(f'{n} + {3:2} = {n+3:2}' + ' '*24 + f'{n+2:2} - {n} = 2')
print(f'{n} + {4:2} = {n+4:2}' + ' '*24 + f'{n+3:2} - {n} = 3')
print(f'{n} + {5:2} = {n+5:2}' + ' '*24 + f'{n+4:2} - {n} = 4')
print(f'{n} + {6:2} = {n+6:2}' + ' '*24 + f'{n+5:2} - {n} = 5')
print(f'{n} + {7:2} = {n+7:2}' + ' '*24 + f'{n+6:2} - {n} = 6')
print(f'{n} + {8:2} = {n+8:2}' + ' '*24 + f'{n+7:2} - {n} = 7')
print(f'{n} + {9:2} = {n+9:2}' + ' '*24 + f'{n+8:2} - {n} = 8')
print(f'{n} + {10:2} = {n+10:2}' + ' '*24 + f'{n+9:2} - {n} = 9')
print('-'*55)
print('Multiplicação' + ' '*24 + 'Divisão')
print(f'{n} x {1:2} = {n*1:2}' + ' '*24 + f'{n*1:2} ÷ {n} = {1:2}')
print(f'{n} x {2:2} = {n*2:2}' + ' '*24 + f'{n*2:2} ÷ {n} = {2:2}')
print(f'{n} x {3:2} = {n*3:2}' + ' '*24 + f'{n*3:2} ÷ {n} = {3:2}')
print(f'{n} x {4:2} = {n*4:2}' + ' '*24 + f'{n*4:2} ÷ {n} = {4:2}')
print(f'{n} x {5:2} = {n*5:2}' + ' '*24 + f'{n*5:2} ÷ {n} = {5:2}')
print(f'{n} x {6:2} = {n*6:2}' + ' '*24 + f'{n*6:2} ÷ {n} = {6:2}')
print(f'{n} x {7:2} = {n*7:2}' + ' '*24 + f'{n*7:2} ÷ {n} = {7:2}')
print(f'{n} x {8:2} = {n*8:2}' + ' '*24 + f'{n*8:2} ÷ {n} = {8:2}')
print(f'{n} x {9:2} = {n*9:2}' + ' '*24 + f'{n*9:2} ÷ {n} = {9:2}')
print(f'{n} x {10:2} = {n*10:2}' + ' '*24 + f'{n*10:2} ÷ {n} = {10:2}')

