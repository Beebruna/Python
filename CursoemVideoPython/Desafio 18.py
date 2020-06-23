'''
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo em graus: '))

print(f'O seno de {angulo}° é {sin(radians(angulo)):.3f}')
print(f'O cosseno de {angulo}° é {cos(radians(angulo)):.3f}')
print(f'A tangente de {angulo}° é {tan(radians(angulo)):.3f}')
