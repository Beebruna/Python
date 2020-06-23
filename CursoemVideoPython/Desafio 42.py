'''
Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:

-Equilátero: todos os lados iguais.
-Isósceles: dois lados iguais.
-Escaleno: todos os lados diferentes.
'''

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < 0 or reta2 < 0 or reta3 < 0:
    print('\nValor Inválido!')
    print('Não EXISTE medida de lado NEGATIVA!')
elif reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 and reta2 == reta3:# ou reta1 == reta2 == reta3
        print('\nÉ um triângulo EQUILÁTERO!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('\nÉ um triângulo ISÓSCELES!')
    else:
        print('\nÉ um triângulo ESCALENO!')
        # reta1 != reta2 != reta3
        #Nesse caso não é testado se reta1 != reta2
        #Para isso, faz-se: reta1 != reta2 != reta3 != reta1
else:
    print('\nAs três retas NÃO podem formar triângulo!')