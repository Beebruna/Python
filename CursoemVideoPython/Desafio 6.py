'''
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.
'''

n = int(input('Digite um número: '))

dobro = n*2
triplo = n*3
raiz = n ** (1/2)

print(f'Número digitado: {n}')
print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raiz quadrada: {raiz:.3f}')
