"""
#Exemplo geral 1
'''
#Tuplas são imutáveis
num = (2, 5, 9, 1)
num[2] = 3
print(num)
'''

#Listas são mutáveis
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
#num[4] = 7 #Não se adiciona valores em listas dessa forma, em php é permitido
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop() #Sem parâmetros remove o último elemento
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)#Para elemento repetido, ele elimina a primeira ocorrência através do ínicio
print(num)

#num.remove(4)#Eliminar valores inexistentes dá erro (Só essa linha)
#Nesse caso, o código abaixo deve ser usado
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
"""

"""
#Exemplo geral 2
#Lista vazia
valores = [] # ou valores = list()

'''
#Inserindo valores manualmente
valores.append(5)
valores.append(9)
valores.append(4)
'''
#print(valores)

'''
for v in valores:
    print(f'{v}...', end='')
'''

#Ler valores pelo teclado
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
"""

"""
#Exemplo geral 3
a = [2, 3, 4, 7]
#b = a #Não faz uma cópia e sim uma ligação
b = a[:]#Isso faz uma cópia e não cria uma ligação
print(f'Lista a: {a}')
print(f'Lista b: {b}')
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')
"""