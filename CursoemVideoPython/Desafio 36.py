'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
tempo = int(input('Digite o tempo de financiamento em anos: '))

valorMensal = valorCasa/(tempo*12)

if valorMensal >= salario*0.7:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
