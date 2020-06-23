'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
'''
sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()

while sexo != 'F' and sexo != 'M':
    print('Valor inválido!\nDigite apenas F para Feminino ou M para Masculino!\nDigite novamente!')
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()
'''
#Correção
sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]#Pega apenas a primeira letra

while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')