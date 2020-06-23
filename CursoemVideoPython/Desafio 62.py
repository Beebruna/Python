'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
'''
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))

print('PA de 10 termos')
print('[', end='')
n = 1
while n != 11:
    if n < 10:
        an = a1 + (n - 1) * r
        print(f'{an}', end=', ')
    else:
        an = a1 + (n - 1) * r
        print(f'{an}', end=']\n')
    n += 1

continuar = 'S'
while continuar == 'S':
    continuar = str(input('\nDeseja mostrar mais termos? [S/N] ')).strip().upper()

    if continuar == 'S':
        t = int(input('Quantos? '))

        if t != 0:
            print(f'\nPA de {t + 10} termos')
            print('[', end='')
            n = 1
            while n != t+11:
                if n < t+10:
                    an = a1 + (n - 1) * r
                    print(f'{an}', end=', ')
                else:
                    an = a1 + (n - 1) * r
                    print(f'{an}', end=']\n')
                n += 1
        else:
            continuar = 'N'
            print('\nAté mais!')
    else:
        print('\nAté mais!')
'''
#Correção
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')