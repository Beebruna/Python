'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
'''

a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))

print('PA de 10 termos')
print('[', end='')
for n in range(1, 11):
    if n < 10:
        print(f'{a1 + (n - 1) * r}', end=', ')
    else:
        print(f'{a1 + (n - 1) * r}', end=']\n')

for n in range(1, 11):
    print(f' \033[0;35ma{n}\033[m', end='  ')