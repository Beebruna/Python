'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

'''
Há infinitos números primos.
Para saber se um número é primo, devemos dividi-lo sucessivamente pelos números primos e verficiar o que acontece:
- Encontrando um resto zero, o número não é primo.
- Se nenhum resto é zero, o número é primo. Nesse caso, só precisamos fazer as divisões até obter um quociente menor ou igual ao divisor.
'''

n = int(input('Digite um número: '))

'''
#Solução 1 com variável bandeira
flag = 0
for i in range(n, 1, -1):
    if n % i == 0 and n != i:
        flag = 1
        break

if flag == 0 and n != 0 and n != 1:
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo!')
'''

#Solução 2 com variável contadoura de divisores
#Correção do prof.
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end='')

print(f'\n\033[mO número {n} foi divisível {cont} vezes.')

if cont == 2:
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo!')
