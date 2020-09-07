'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

ver imagem 7 e 8
'''
from datetime import datetime

nome = str(input('Nome: ')).strip()
anoNascimento = int(input('Ano de Nascimento: '))
carteiraTrabalho = int(input('Carteira de Trabalho (0 não tem): '))

idade = datetime.now().year - anoNascimento

dict = {'nome': nome,
        'idade': idade,
        'ctps': carteiraTrabalho,
        }

if carteiraTrabalho != 0:
    dict['contratacao'] = int(input('Ano de Contratação: '))
    dict['salario'] = float(input('Salário: R$ '))

    #idade de aposentadoria 65
    anoAposentadoria = dict['contratacao'] + 35
    dict['aposentadoria'] = idade + anoAposentadoria - datetime.now().year

print('-='*30)
for k, v in dict.items():
    print(f'    - {k} tem valor: {v}')
    





