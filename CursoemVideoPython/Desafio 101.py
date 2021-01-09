'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

from datetime import date

def voto(anoNascimento):

    idade = date.today().year - anoNascimento

    if idade < 16:
        return idade, 'NEGADO'
    else:
        if 16 <= idade < 18 or idade >= 70:
            return idade, 'OPCIONAL'
        else:
            return idade, 'OBRIGATÓRIO'


print('-'*30)
anoNascimento = int(input('Em que ano você nasceu? '))
idade, voto = voto(anoNascimento)
print(f'Com {idade} anos: VOTO {voto}.')

