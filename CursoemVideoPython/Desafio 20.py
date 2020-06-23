'''
O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'\n Ordem de Apresentação ')
print(alunos)
'''
# Solução mediana, pois possibilita a repetição de pessoas
aluno = choice([a1, a2, a3, a4])
print(f'1° - {aluno}')

aluno = choice([a1, a2, a3, a4])
print(f'2° - {aluno}')

aluno = choice([a1, a2, a3, a4])
print(f'3° - {aluno}')

aluno = choice([a1, a2, a3, a4])
print(f'4° - {aluno}')
'''



