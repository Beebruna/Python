'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome "Santo".
'''

cidade = str(input('Digite o nome da cidade: ')).strip()

palavra = cidade.split()
inicio = palavra[0].capitalize()
#igual = 'Santo ' in inicio #não é legal, pois apenas 'Santo' daria falso.

print(f'A cidade começa com "Santo"? {inicio == "Santo"}')

'''
#Correção
print(cidade[:5].upper() == 'SANTO')#'Santorini' dá verdadeiro
'''
