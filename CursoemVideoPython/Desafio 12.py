'''
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
'''

preco = float(input('Digite o preço do produto: R$ '))

novoPreco = preco*0.95

print(f'O preço com 5% de desconto é R${novoPreco:.2f}')