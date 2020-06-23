#import math #->importa toda a biblioteca
#from math import sqrt #dessa forma, não é necessário chamar math.sqrt(), apenas chamar direto sqrt()
from math import sqrt, floor #utiliza duas funcionalidades

num = int(input('Digite um número: '))

raiz = sqrt(num) #utilizando from math import sqrt

#raiz = math.sqrt(num) #utilizando import math

print(f'A raiz de {num} é igual a {floor(raiz):.2f}')

'''
#arredonda a raiz para cima
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

#arredonda a raiz para baixo
print(f'A raiz de {num} é igual a {math.floor(raiz)}')
'''

