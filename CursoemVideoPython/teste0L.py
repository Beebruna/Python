for c in range(1,6):# imprime 'Oi' 5 vezes, de 1 a 5
    print('Oi')
print('FIM')

for c in range(1,6):
    print(c)
print('FIM')

for c in range(6,0,-1):# imprime os números em ordem decrescente de 6 a 1
    print(c)
print('FIM')

for c in range(0,7,2): # imprime de 0 a 6 pulando de 2 em 2
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n #s += n
print(f'O somatório de todos os valores foi {s}')