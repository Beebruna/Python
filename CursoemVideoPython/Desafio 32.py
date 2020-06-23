'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

'''
Os números correspondentes a anos bissextos são divisíveis por 4. Mas atenção: 
os anos terminados em 00 só são bissextos quando são divisíveis por 400.
'''
from datetime import date

ano = int(input('Digite um ano: [ou 0 para o ano atual.] '))

if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%400 == 0:
    print(f'{ano} É BISSEXTO!')
else:
    if ano%4 == 0 and ano%100 != 0:
        print(f'{ano} É BISSEXTO!')
    else:
        print(f'{ano} Não é BISSEXTO!')

#ou
#if ano%4 == 0 and ano%100 != 0 or ano%400 == 0: