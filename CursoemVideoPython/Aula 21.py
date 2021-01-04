#help(print)
#print(input.__doc__) #ou help(input)
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """

    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)

help(contador)
'''

'''
#Parämetros opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """

    s = a + b + c
    print(f'A soma vale {s}')

somar(2,3,5)
somar(2,3)
somar(3)
somar()
somar(b=4, c=2)
somar(c=3, a=2)
'''

#Escopo de Variáveis
'''
def teste():
    x = 8 #Escopo Local, Variável Local (existe apenas dentro da função)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2 #Escopo Global, Variável Global (assume o mesmo valor em todo o programa)
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}') #Não funciona, pois x é local
'''

'''
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
'''

#Return
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')
