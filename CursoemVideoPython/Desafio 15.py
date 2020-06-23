'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.
'''

qtdPer = float(input('Digite a quantidade de km percorridos: '))
qtdDia = int(input('Digite a quantidade de dias do aluguel: '))

precoPagar = 60*qtdDia + 0.15*qtdPer

print(f'O preço a pagar é R$ {precoPagar:.2f}')