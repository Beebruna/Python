'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(valor, show=False):

    """
    -> Calcula o Fatorial de um número.
    :param valor: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número passado.
    """

    fatorial = 1

    for i in range(valor, 0, -1):
        fatorial *= i

        if show:
            print(i, end='')

            if i == 1:
                print(end=' = ')
            else:
                print(end=' x ')

    return fatorial


valor = int(input('Digite um valor: '))
show = str(input('Deseja ver os cálculos? [S/N] '))

if show in 'Ss':
    print(f'O fatorial de {valor} é:')
    show = True
    print(f'{fatorial(valor, show)}')
else:
    print(f'O fatorial de {valor} é: {fatorial(valor)}')

input()