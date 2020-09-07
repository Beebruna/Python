'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    return largura*comprimento


print('Controle de Terrenos')
print('-'*20)

largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))
print(f'A área de um terreno {largura:.2f} x {comprimento:.2f} é de {area(largura, comprimento):.2f} m².')