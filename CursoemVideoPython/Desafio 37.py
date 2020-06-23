'''
Escreva um programa que leia um número inteiro e peça para o usuário escolher qual
será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
base = int(input("""Para qual base deseja converter?
                 1. Binário
                 2. Octal
                 3. Hexadecimal
                 Resposta: """))
if base == 1:
    print(f'Em binário: {bin(num)[2:]}')#TIRA O 0b
elif base == 2:
    print(f'Em Octal: {oct(num)[2:]}')#TIRA O 0o
elif base == 3:
    print(f'Em hexadecimal: {hex(num)[2:]}')#TIRA O 0x
else:
    print('Opção INVÁLIDA!')