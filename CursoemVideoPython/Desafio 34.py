'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o salário: R$ '))

if salario < 0:
    print('Valor inválido!')
else:
    if salario <= 1250:
        print(f'O aumento será de R${salario*0.15} e passará a ser R${salario + salario*0.15}')
    else:
        print(f'O aumento será de R${salario * 0.10} e passará a ser R${salario + salario * 0.10}')