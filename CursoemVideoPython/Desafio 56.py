'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos.
'''

somaIdade = 0
contIdade = 0
contHomem = 0
contMulher = 0

for i in range(4):
    print('-'*5 + f' {i+1}ª PESSOA ' + '-'*5)
    nome = str(input('Digite o nome: ')).strip().capitalize()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M ou F): ')).strip().upper()

    somaIdade += idade
    
    if sexo == 'M':#ou <sexo in 'Mm'> sem precisar do upper()
        contHomem += 1

        if contHomem == 1:
            maior = idade
            nomeMaisVelho = nome
        elif maior < idade:
            maior = idade
            nomeMaisVelho = nome
    
    if sexo == 'F':
        contMulher += 1

        if idade < 20:
            contIdade += 1

media = somaIdade/4
print(f'\nA média de idade do grupo é: {media:.2f}')

if contHomem == 0:
    print('Não há homens!')
else:
    print(f'{nomeMaisVelho} é o homem mais velho.')

if contMulher == 0:
    print('Não há mulheres!')
elif contIdade == 0:
    print('Não há mulheres com menos de 20 anos de idade!')
elif contIdade > 1:
    print(f'{contIdade} mulheres tem menos de 20 anos de idade.')
else:
    print(f'{contIdade} mulher tem menos de 20 anos de idade.')
