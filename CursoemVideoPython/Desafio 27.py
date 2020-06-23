'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.

Ex.:
Ana Maria de Souza

primeiro = Ana
último = Souza
'''

nome = str(input('Digite o nome completo de uma pessoa: ')).strip().title().split()

print(f'\nPrimeiro nome = {nome[0]}')
print(f'Último nome = {nome[len(nome)-1]}')
#ou
print(f'Último nome = {nome[-1]}')