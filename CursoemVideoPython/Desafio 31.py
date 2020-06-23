'''
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço
da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45/km para viagens
mais longas.
'''

dist = float(input('Digite a distância da viagem em km: '))

if 0 <= dist <= 200:
    preco = dist*0.5
    print(f'O preço da viagem será de R${preco:.2f}')
else:
    if dist > 200:
        preco = dist*0.45
        print(f'O preço da viagem será de R${preco:.2f}')
    else:
        print('Valor Inválido!')

#simplificado
#preço = distância*0.50 if distância <= 200 else distância*0.45