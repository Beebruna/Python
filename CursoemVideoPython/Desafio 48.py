'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0

'''
#Na raça
for i in range(1, 500):
    if i%2 != 0:
        if i%3 == 0:
            soma = soma + i

print(f'A soma de todos os números ímpares que são múltiplos de três no intervalo de [1,500] é: {soma}')
'''
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'\nA soma de todos os números ímpares que são múltiplos de três no intervalo de [1,500] é: {soma}')
print(f'Foram somados {cont} valores.')