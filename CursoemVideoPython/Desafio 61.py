'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print('PA de 10 termos')
print('[', end='')
n = 1
while n != 11:
    print(f'{a1 + (n - 1) * r}', end='')
    print(',' if n < 10 else ']', end=' ')
    n += 1