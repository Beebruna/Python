'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela  cada um dos dígitos
separados.
Ex.:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

num = int(input('Digite um número entre 0 e 9999: '))
'''
unidade = num%10
dezena = (num%100)//10
centena = (num%1000)//100
milhar = num//1000
'''
#Correção
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'\nUnidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')