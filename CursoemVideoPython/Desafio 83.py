'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta.
'''

#Melhorar esse programa para que ele valide uma expressão corretamente!!!

expressao = str(input(('Digite uma expressão: '))).strip()

pAberto = expressao.count('(')
pFechado = expressao.count(')')

if pAberto > pFechado:
    print('Existem parênteses que não foram fechados!')
elif pAberto < pFechado:
    print('Existem parênteses fechados em excesso!')
else:
    print('Expressão Válida!')

'''
#Estava tentando analisar se uma expressão foi ou não escrita corretamente
for p, e in enumerate(expressao):
    if e == '(':
        if expressao(p+1) not in '0123456789':
            print('Expressão Inválida!')
            print('Depois de um parênteses aberto deverá vir um número!')
            break
    if e in '+-*/':
        if expressao(p+1) not in '0123456789':
            print('Expressão Inválida!')
            print('Depois de um operador deverá vir um número!')
            break

    if e == ')':
        if expressao(p-1) not in '0123456789':
            print('Expressão Inválida!')
            print('Antes de um parênteses fechado deverá vir um número!')
            break
'''
'''
#Correção
expr = str(input('Digite a expressão: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
'''



