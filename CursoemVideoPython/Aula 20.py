""""
#Exemplo geral 1
'''
#Código que será substituído pela função soma()
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

#Programa Principal
soma(4, 5)#uma cópia é passada
soma(8, 9)
soma(2, 1)
soma(a = 3, b = 1)#Os parâmetros podem ser explicitados.
soma(b = 3, a = 1)#A ordem dos parâmetros podem ser invertidos, desde que sejam explicitados.
#É importante que os DOIS sejam explicitados, caso desejado, e não apenas um dos dois.
"""
'''
#Exemplo geral 2
def contador(*num):#desempacotamento
    print(num)


#Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
#Exemplo geral 3
def dobra(lst):
    pos = 0

    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
