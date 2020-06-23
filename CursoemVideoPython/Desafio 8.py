'''
Escreva um programa que leia um valor em metros e o exiba covertido
em centímetros e milímetros.
'''

n = float(input('Digite um valor em metro: '))

milimetro = n*1000
centimetro = n*100
decimetro = n*10
decametro = n/10
hectometro = n/100
kilometro = n/1000

print(f'Valor em milímetro: {milimetro}mm')
print(f'Valor em centímetros: {centimetro}cm')
print(f'Valor em decímetros: {decimetro}dm')
print(f'Valor em metros: {n}m')
print(f'Valor em decâmetro: {decametro}dam')
print(f'Valor em hectômetro: {hectometro}hm')
print(f'Valor em kilômetro: {kilometro}km')