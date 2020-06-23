'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

'''
tupla = ('Banana', 1.75, 'Melancia', 0.50, 'Morango', 0.25, 'Pêra', 1.50, 'Uva', 2.25, 'Melão', 2.50)

print('Produtos' + ' '*17 + 'Preços')

j = 1
for i in tupla[::2]:
    print(f'{i:9}' + '-'*15 + f' R$ {tupla[j]:.2f}')
    j += 2
'''

#Correção
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)