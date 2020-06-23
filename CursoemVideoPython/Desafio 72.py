'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de 0 até 20.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))

while num < 0 or num > 20:
    print('Opção Inválida! Tente Novamente!')
    num = int(input('Digite um número entre 0 e 20: '))

print(f'O número {num} por extenso é: {numeros[num]}')

'''
#Correção
while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if 0 <= num <= 20:
        break

    print('Opção Inválida! Tente Novamente!')
'''

'''
Obs.: Colocá-lo para repetir com condição de parada.
'''