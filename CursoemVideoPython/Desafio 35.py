'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
'''

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < 0 or reta2 < 0 or reta3 < 0:
    print('\nValor Inválido!')
    print('Não EXISTE medida de lado NEGATIVA!')
else:
    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
        print('\nAs três retas podem formar triângulo!')
    else:
        print('\nAs três retas NÃO podem formar triângulo!')