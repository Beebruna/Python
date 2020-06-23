'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente.
'''

#Uma lista com duas listas internas

'''
#Solução com 1 lista apenas
#Mas deveria ter duas listas internas

lista = []

contP = 0
for i in range(1, 8):
    num = (int(input(f'Digite o {i}º número: ')))

    if num%2 == 0:
        lista.insert(0, num)
        contP += 1
    else:
        lista.append(num)

for i in range(contP):
    for j in range(i+1, contP):
        if lista[i] > lista[j]:
            num = lista[i]
            lista[i] = lista[j]
            lista[j] = num

for i in range(contP, len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            num = lista[i]
            lista[i] = lista[j]
            lista[j] = num

print(f'\nPares: {lista[:contP]}')
print(f'Ímpares: {lista[contP:]}')
'''

'''
#Solução com duas listass internas
lista = []
tempP = []
tempI = []

for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))

    if num % 2 == 0:
        tempP.append(num)
    else:
        tempI.append(num)

lista.append(tempP[:])
lista.append(tempI[:])
tempP.clear()
tempI.clear()

lista[0].sort()
print(f'\nPares: {lista[0]}')
lista[1].sort()
print(f'Ímpares: {lista[1]}')
'''

#Solução do prof.
num = [[],[]]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
