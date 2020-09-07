'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint
from time import sleep

def sorteia(lista):

    for i in range(5):
        lista.append(randint(1, 100))

    return lista
    
def somaPar(lista):
    soma = 0

    for i in lista:
        if i%2 == 0:
            soma += i
    
    return soma


numeros = list()

print(f'Sorteando 5 valores da lista: {sorteia(numeros)}')
print(f'Somando os valores pares de {numeros}, temos {somaPar(numeros)}')


'''
#Resolução do prof.
def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor%2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
'''