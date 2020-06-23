'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('5 primeiros colocados:')
print(times[:5])
print('\n4 últimos colocados:')
print(times[16:])#ou times[-4]
print('\nTimes em Ordem Alfabética:')
print(sorted(times))
print(f'\nA Chapecoense está na {times.index("Chapecoense") + 1}ª posição')