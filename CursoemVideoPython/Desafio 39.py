'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:

-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar;
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

ano = int(input('Digite a data de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano

print(f'Você tem {idade} anos de idade.')

if idade < 18:
    saldo = 18 - idade
    print(f'''Você ainda vai se alistar ao serviço militar!
    Ainda faltam {saldo} anos.''')
    print(f'Seu alistamento será em {anoAtual + saldo}')
elif idade == 18:
    print('É hora de se alistar ao serviço militar!')
else:
    saldo = idade - 18
    print(f'''Você já passou do tempo de alistamento!
    Faz {saldo} anos.''')
    print(f'Seu alistamento foi em {anoAtual - saldo}.')

