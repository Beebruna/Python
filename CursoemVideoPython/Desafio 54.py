'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores.
'''

from datetime import date

atual = date.today().year
cont = 0

for i in range(7):
    ano = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))

    if atual - ano < 18:
        cont += 1

print(f'\n{7 - cont} pessoas já são maiores de idade.')
print(f'{cont} pessoas ainda não atingiram a maior de idade.')
