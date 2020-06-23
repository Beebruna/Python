'''
nome = input('Qual é o seu nome? ')
#nome escrito em 20 caracteres (espaços)
print('Prazer em te conhecer {:20}!'.format(nome))
#nome escrito em 20 caracteres (espaços) alinhado à direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#nome escrito em 20 caracteres (espaços) alinhado à esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#nome escrito em 20 caracteres (espaços) centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))
#nome escrito em 20 caracteres (espaços) centralizado e colocando '=' em volta
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1/ n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
#print('A soma vale {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='>>>')
# {:.3f} - > 3 casas decimais flutuantes
# \n para quebrar linha (nova linha;)
# end=' ' ou qualuer coisa dentro de '' -> não quebra linha de um print para outro e ainda insere o que está dentro de ''
print('Divisão inteira {} e potência {}'.format(di,e))
