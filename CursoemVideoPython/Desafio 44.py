'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto.
-em até 2x no cartão: preço normal.
-3x ou mais no cartão: 20% de juros.
'''

preco = float(input('Digite o preço do produto: R$'))

pagamento = int(input("""Escolha a forma de pagamento:
                        1. À vista no Dinheiro/Cheque;
                        2. À vista no cartão;
                        3. 2x no cartão;
                        4. 3x ou mais no cartão.
                        Resposta: """))

if pagamento == 1:
    print(f'\nValor a pagar: R${preco*0.9:.2f} com DESCONTO DE 10%')
elif pagamento == 2:
    print(f'\nValor a pagar: R${preco * 0.95:.2f} com DESCONTO DE 5%')
elif pagamento == 3:
    parcela = preco/2
    print(f'\nCompra parcelada em 2x no valor de R${parcela:.2f} SEM JUROS!')
    print(f'Valor a pagar: R${preco:.2f}')
elif pagamento == 4:
    parcela = (preco*1.2)/3
    print(f'\nCompra parcelada em 3x no valor de R${parcela:.2f} COM JUROS DE 20%')
    print(f'Valor total a pagar: R${preco * 1.2:.2f}')
else:
    print('\n\033[1;31mOpção INVÁLIDA!\033[m')