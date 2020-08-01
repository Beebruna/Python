'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

Ex.:
Nome: Gláucia
Média de Gláucia: 8.5

Nome é igual a Gláucia
Média é igual a 8.5
Situação é igual a Aprovado
'''

dict = {}
dict['nome'] = str(input('Digite o nome: ')).strip()
dict['media'] = float(input('Digite a média: '))

if dict['media'] >= 6.0:
    situacao = 'Aprovado(a)'
else:
    situacao = 'Reprovado(a)'

dict['situacao'] = situacao

print('\n***************************************')
print(f'Nome: {dict["nome"]}')
print(f'Média de {dict["nome"]}: {dict["media"]:.2f}')
print(f'Situação: {dict["situacao"]}')
