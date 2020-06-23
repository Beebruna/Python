'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo.
'''

while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    
    if n < 0:
        break

    print('\033[32m=\033[m' * 38)
    for i in range(1, 11):
        print(f'\033[36m{n}\033[m \033[35mx\033[m \033[36m{i:2}\033[m \033[35m=\033[m \033[36m{n*i:2}\033[m')
    print('\033[32m=\033[m' * 38)

print('\033[32m=\033[m' * 38)
print('\033[31mAté mais!\033[m')
print('\033[32m=\033[m' * 38)