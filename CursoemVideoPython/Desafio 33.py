'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
'''
if num1 == num2 and num1 == num3 and num2 == num3:
    print('\nOs números são todos iguais!')
else:
    if num1 == num2 and num1 > num3:
        print(f'\nO número {num1} é o maior de todos!')
        print(f'O número {num3} é o menor de todos!')
    else:
        if num1 == num2 and num1 < num3:
            print(f'\nO número {num3} é o maior de todos!')
            print(f'O número {num1} é o menor de todos!')
        else:
            if num1 == num3 and num1 > num2:
                print(f'\nO número {num1} é o maior de todos!')
                print(f'O número {num2} é o menor de todos!')
            else:
                if num1 == num3 and num1 < num2:
                    print(f'\nO número {num2} é o maior de todos!')
                    print(f'O número {num1} é o menor de todos!')
                else:
                    if num2 == num3 and num2 > num1:
                        print(f'\nO número {num2} é o maior de todos!')
                        print(f'O número {num1} é o menor de todos!')
                    else:
                        if num2 == num3 and num2 < num1:
                            print(f'\nO número {num1} é o maior de todos!')
                            print(f'O número {num2} é o menor de todos!')
                        else:
                            if num1 > num2 and num1 > num3:
                                print(f'\nO número {num1} é o maior de todos!')

                                if num2 < num3:
                                    print(f'O número {num2} é o menor de todos!')
                                else:
                                    print(f'O número {num3} é o menor de todos!')
                            else:
                                if num2 > num1 and num2 > num3:
                                    print(f'\nO número {num2} é o maior de todos!')

                                    if num1 < num3:
                                        print(f'O número {num1} é o menor de todos!')
                                    else:
                                        print(f'O número {num3} é o menor de todos!')
                                else:
                                    print(f'\nO número {num3} é o maior de todos!')

                                    if num1 < num2:
                                        print(f'O número {num1} é o menor de todos!')
                                    else:
                                        print(f'O número {num2} é o menor de todos!')
'''

#Correção
if num1 == num2 and num1 == num3 and num2 == num3:
    print('\nOs números são todos iguais!')
else:
    menor = num1

    if num2 < num1 and num2 < num3:
        menor = num2
    else:
        if num3 < num1 and num3 < num2:
            menor = num3

    maior = num1

    if num2 > num1 and num2 > num3:
        maior = num2
    else:
        if num3 > num1 and num3 > num2:
            maior = num3

    print(f'\n{menor} é o menor número.')
    print(f'{maior} é o maior número.')
