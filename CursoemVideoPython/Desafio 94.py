'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.

ver imagem 10
'''
dict = dict() #Armazena 1 pessoa
lista = list() #Armazena todas as pessoas
soma = media = 0 #Soma as idades

while True:
    dict['nome'] = str(input('Nome: ')).strip()
    
    while True:
        dict['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()[0]
        
        if dict['sexo'] in 'fm':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    dict['idade'] = int(input('Idade: '))

    soma += dict['idade']

    lista.append(dict.copy()) #Insere o dicionário na lista
    dict.clear() #limpa o dicionário
    
    print('='*30)
    while True:
        valor = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        if valor in 'sn':
            break
        
        print('ERRO! Por favor, digite apenas S ou N!')
        print('='*30)
    
    if valor == 'n':
        print('Até mais!')
        print('='*30)
        break

media = soma/len(lista)

print(f'A) O grupo tem {len(lista)} pessoas.')
print(f'B) A média de idade é de {media:.2f} anos.')

print('C As mulheres cadastradas foram: ', end=' ')
for i in lista:
    if i['sexo'] == 'f':
         print(i['nome'], end=' ')

print('\nD) Lista das pessoas que estão acima da média:')
for d in lista:
    if d['idade'] >= media:
        print('      ', end='')
        for k, v in d.items():
            print(f'{k} = {v}; ', end=' ')
        print()