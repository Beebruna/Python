'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

frase = str(input('Digite uma frase: ')).strip().upper()

flag = 0
c = len(frase)
t = len(frase)-1

for i in range(c):
    if frase[i] == ' ':
        i += 1
        t += 1
    if frase[t-i] == ' ':
        t -= 1

    if i == (t - i):
        break
    elif frase[i] != frase[t - i]:
        flag = 1
        break

if flag == 1:
    print(f'< {frase} > não é um palíndromo!')
else:
    print(f'< {frase} > é um palíndromo!')

'''
#Correção 1 do prof.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
'''
'''
#Correção 2 do prof.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
'''