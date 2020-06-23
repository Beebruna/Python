'''
Um professor quer sortear um dos seus quatro alunos para apagar o
quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido.
'''

from random import choice

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

escolhido = choice([a1, a2, a3, a4])

print(f'\n{escolhido} vai apagar o quadro.')

# para o python, uma lista fica entre []
