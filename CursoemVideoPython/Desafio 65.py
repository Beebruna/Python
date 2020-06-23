'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

cont = soma = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    soma += num

    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    print(end='\n')

media = soma/cont
print(f'A média dos números digitados é {media:.2f}')
print(f'O maior valor lido é {maior}.')
print(f'O menor valor lido é {menor}.')

