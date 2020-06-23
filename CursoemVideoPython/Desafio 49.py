'''
Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só
que agora utilizando um laço for.
'''


num = int(input('Digite um número: '))

print('-'*10 + ' Tabuada ' + '-'*10)
print('***************************************************************')
print('   Adição ' + ' '*22 + ' Subtração')
print('***************************************************************')

for i in range(1, 11):
    print(f'{num} + {i:2} = {num + i:2}' + ' '*20 + f'{num-1+i:2} - {num} = {i - 1:2}')

print('***************************************************************')
print('Multiplicação ' + ' '*18 + ' Divisão')
print('***************************************************************')

for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i:2}' + ' '*20 + f'{i*num:2} ÷ {num} = {i:2}')
