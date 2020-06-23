'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade < 0:
    print('Valor Inválido!')
else:
    if velocidade > 80.00:
        print(f'Você foi multado por ultrapassar o limite de 80km/h')
        multa = (velocidade - 80.00)*7.00
        print(f'Sua multa é de R${multa:.2f}')
print('Você está dentro do limite de 80km/k!')