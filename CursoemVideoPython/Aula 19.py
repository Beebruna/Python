'''
#Exemplo geral 1

#declaração de dicionário
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
#print(pessoas[0])#dá  erro, pois não existe índice 0
print(pessoas['nome'])#mostra o conteúdo do índice/key nome
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo'] #deleta um item

pessoas['nome'] = 'Leandro' #Muda o valor de um item

pessoas['peso'] = 98.5 #Adiciona um item

for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
#Exemplo geral 2

brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

#Exemplo geral 3

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

#print(brasil) ou
'''
for e in brasil:#para lista
    for k, v in e.items(): #para o dicionário
        print(f'O campo {k} tem valor {v}.')
'''
#ou
for e in brasil:#para lista
    for v in e.values(): #para o dicionário
        print(v, end=' ')
    print()