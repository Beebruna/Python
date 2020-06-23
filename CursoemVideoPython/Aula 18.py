"""
#Exemplo Geral 1

teste = list()

teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
'''
galera.append(teste)
print(galera)

#A lista galera também muda
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
'''
#Deve-se fazer uma cópia do elemento de lista para que seja o único a ser alterado
galera.append(teste[:])#Adiciona uma cópia da lista original

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])

print(galera)
"""
'''
#Exemplo Geral 2
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(p)#mostra os elementos da lista galera

for p in galera:
    print(p[0])#mostra os primeiros itens dos elementos-lista

for p in galera:
    print(p[1])#mostra os segundos itens dos elementos-lista

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

#Exemplo Geral 3
galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

'''
#Clear em dados exclui também a lista galera
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado)
    dado.clear()
print(galera)
'''

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')