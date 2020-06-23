'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas;
O nome com todas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo: ')).strip()

print('\nNome todo em maiúsculo:', nome.upper())
print('Nome todo em minúsculo:', nome.lower())
print(f'Quantidade de letras = {len(nome) - nome.count(" ")}')
print('O primeiro nome tem', len(nome.split()[0]), 'letras')
#ou
print('O primeiro nome tem', nome.find(" "), 'letras')

