'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois
disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

'''
palavras = ('amarelo', 'bonito', 'imagem', 'cor', 'uva', 'cachorro', 'carro', 'casa', 'agua', 'passaro', 'cabelo', 'vasilha', 'frances')

for i in range(len(palavras)):
    print(f'{palavras[i]}: ', end='')

    for j in range(len(palavras[i])):
        if palavras[i][j] in 'aeiou':
            print(f'{palavras[i][j]}', end=' ')
    print('')
'''
#Correção

palavras = ('aprender', 'programar', 'linguaguem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
