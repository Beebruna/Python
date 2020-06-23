'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

nome = str(input('Digite um nome de pessoa: ')).title().split()

print(f'\nTem "Silva" no nome? {"Silva" in nome}')

#Essa forma evita que 'Silvana' seja aceita