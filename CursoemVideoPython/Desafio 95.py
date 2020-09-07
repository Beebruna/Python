'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

ver imagem 11 e 12
'''
dict = {}
lista = []
gols = []

while True:
    dict['nome'] = str(input('Nome do jogador: ')).strip()

    qtdPartida = int(input(f'Quantas partidas {dict["nome"]} jogou?: '))

    for i in range(qtdPartida):
        gols.append(int(input(f'\tQuantos gols na partida {i}?: ')))

    dict['gols'] = gols[:]
    dict['total'] = sum(gols)

    lista.append(dict.copy())
    gols.clear()
    dict.clear()
    
    print('='*50)
    while True:
        valor = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        if valor in 'sn':
            break
        
        print('Valor inválido! Digite novamente!')
        print('='*50)
    
    if valor == 'n':
        print('='*50)
        break

print('cod nome' + ' '*10 + 'gols' + ' '*10 + 'total')
print('-'*50)

'''
for i in range(len(lista)):
    print(f'{i} {str(lista[i]["nome"]):<15} {str(lista[i]["gols"]):<15} {lista[i]["total"]}')
'''
#ou
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')

    for d in v.values():
        print(f'{str(d):15}', end='')
    print()

print('-'*50)

while True:
    dado = int(input('Mostrar dados de qual jogador? '))

    if dado >= len(lista):
        print(f'ERRO! Não existe jogador com código {dado}! Tente novamente.')
        print('='*50)

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[dado]["nome"]}:')

        for i, g in enumerate(lista[dado]['gols']):
            print(f'\tNo jogo {i+1} fez {g} gols.')

    print('='*50)
    while True:
        valor = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        if valor in 'sn':
            break
        
        print('Valor inválido! Digite novamente!')
        print('='*50)
    
    if valor == 'n':
        print('='*50)
        print('<< VOLTE SEMPRE >>')
        break
