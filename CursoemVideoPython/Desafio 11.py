'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
expoente 2 = alt + 0178
'''

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura*altura
qtdTinta = area/2

print(f'\nÉ necessário de {qtdTinta:.2f}l de tinta para pintar uma parede de {area:.2f}m² de área')
