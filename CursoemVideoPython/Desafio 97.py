'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')

Saída:
-----------
Olá, Mundo!
-----------
as linhas acompanham o tamanho da mensagem
'''

def escreva(texto):
    print('~'*(len(texto) + 4))
    print(f'  {texto}')
    print('~'*(len(texto) + 4))


escreva('Gustavo Guanabara')
escreva('CeV')
escreva('Curso de Python no Youtube')