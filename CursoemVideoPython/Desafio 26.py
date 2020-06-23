'''
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A";
Em que posição ela aparece na primeira vez;
Em que posição ela aparece na última vez.
'''

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'\nA letra "A" aparece {frase.count("A")} vezes.')
print(f'Na primeira vez na posição {frase.find("A")+1}')
print(f'Na última vez na posição {frase.rfind("A")+1}')


