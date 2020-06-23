'''
Faça  um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.
'''

salario = float(input('Digite o salário: R$ '))

novoSalario = salario*1.15

print(f'O novo salário com 15% de aumento é R${novoSalario:.2f}')
