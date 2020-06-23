'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
'''

# listona, listinha, listinha
# lista alunos, cada elemento contém dados de 1 aluno: nome, notas e média, e
# notas são um componente extra, ou seja, uma lista dentro da lista, dentro da lista.

'''
alunos = []
notas = []  # tamanho 2, n1 e n2
aluno = []  # tamanho 3, nome, notas e media

soma = media = 0

while True:
    aluno.append(str(input('Digite o nome: ')))

    for i in range(2):
        notas.append(float(input(f'Digite a {i + 1}º nota: ')))  # 2 notas por lista
        soma += notas[i]

    media = soma / 2

    aluno.append(notas[:])
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    soma = media = 0

    print('*********************************')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    print('*********************************')


    while continuar not in 'sn':
        print('Opção Inválida! Tente Novamente!')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
        print('*********************************')

    if continuar in 'n':
        print('Até Mais!')
        print('*********************************')
        break
alunos.sort()

print()
print('-' * 13 + ' BOLETIM ' + '-' * 14)
print('NOME' + ' ' * 9 + 'MÉDIA')

for i in range(len(alunos)):
    print(f'{alunos[i][0].title():13}', end='')  # nome

    print(f'{alunos[i][2]:.2f}')  # media

print()
while True:
    individual = str(input('Deseja ver as notas de qual aluno? ')).strip().lower()
    print()
    print('-'*12 + f' Boletim {individual.title() }' + '-'*11)

    print('NOME' + ' ' * 10 + 'N1' + ' ' * 7 + 'N2')
    for i in alunos:
        if individual in i:
            print(f'{i[0].capitalize():13}', end='')  # nome

            for j in range(2):
                print(f'{i[1][j]:.2f}', end=' ' * 5)  # notas

    print()
    print('*********************************')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    print('*********************************')

    while continuar not in 'sn':
        print('Opção Inválida! Tente Novamente!')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
        print('*********************************')

    if continuar in 'n':
        print('Até Mais!')
        print('*********************************')
        break
'''

#Solução
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opc == 999:
        print('FINALIZANDO...')
        break

    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<< VOLTE SEMPRE >>>')