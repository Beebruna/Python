n1 = int(input('Digite um Valor: '))
n2 = int(input('Digite outro: '))
#print(type(n1))#função type retorna o tipo primitivo.
#para retornar um número é preciso fazer um casting.
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
#Esse método susbstitui o método de cima dele.
#As numerações não são obrigatórias.
'''
#Outra forma a partir do python 3.7
print(f'A soma de {n1} e {n2} é {s}')
#Colocarum f antes das '' e as variáveis dentro das chaves
'''


