"""
#Exemplo geral 1
#Declaração de uma tupla (Com parênteses)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

'''
print(lanche)#Mostra todos os elementos da tupla

#Declaração de uma tupla (ou Sem parênteses)
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

print(lanche)#Mostra todos os elementos da tupla
#Referenciar um elemento
print(lanche[1])# Mostra o elemento na posição 1
print(lanche[3])# Mostra o elemento na posição 3
print(lanche[-1])#Mostra o último elemento (Que é indexado por 3 ou -1)
print(lanche[-2])#Mostra o penúltimo elemento (Que é indexado por 2 ou -2)
print(lanche[1:3])#Mostra o elemento da posição 1 até o elemento da posição 2
print(lanche[2:])#Mostra o elemento da posição 2 até o elemento final da tupla
print(lanche[:2])#Mostra o elemento da posição 0 até o elemento da posição 1
print(lanche[-2:])#Mostra o elemento da posição -2 ( ou 2) até o elemento final da tupla
print(lanche[-3:])#Mostra o elemento da posição -3 (ou 1) até o elemento final da tupla
'''

#Tuplas são imutáveis
'''
lanche[1] = 'Refrigerante'#Isso não é permitido
print(lanche[1])# Dá erro
'''

'''
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
'''

'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
'''

'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
'''

'''
print(len(lanche))#A função len() retorna a quantidade de itens totais na tupla
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(len(lanche))

for cont in range(0, len(lanche)):
    print(cont)
    print(lanche[cont])
print('Comi pra caramba!')
'''

'''
print(sorted(lanche))# A função sorted ordena a tupla,
print(lanche)#mas não muda a original, pois as tuplas são imutáveis
'''
"""

"""
#Exemplo geral 2

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Une a tupla a com a tupla b
d = b + a #A ordem importa

print(a)
print(b)
print(c)
print(d)
print(len(c))
print(d.count(5))#A função count() retorna a quantidade de vezes que um determinado elemento aparece.
print(d.count(4))
print(d.count(9))
print(d.index(8))#A função index() retorna a posição de um determinado elemento na sua primeira ocorrência
print(d.index(4))
print(d.index(2))
print(d.index(2, 4))#A partir da posição 4. Isso se chama deslocamento
print(d.index(5))
print(d.index(5, 1))# Procura a posição do elemento 5 a partir da posição 1
"""

"""
#Exemplo geral 3
#As tuplas aceitam qualquer dado de tipos diferentes, em uma mesma declaração, diferente de vetores em outras linguagens
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)#Apaga a tupla da memória
#del(pessoa[0])#Não é permitido
print(pessoa)
"""