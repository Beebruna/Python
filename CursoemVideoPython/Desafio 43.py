'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do Peso.
-Entre 18.5 e 25: Peso ideal.
-25 até 30: Sobrepeso.
-30 até 40: Obesidade.
-Acima de 40: Obesidade mórbida.
'''

massa = float(input('Digite a sua massa corporal: (kg)  '))

altura = float(input('Digite a sua altura: (m) '))

imc = massa/altura**2

if imc < 18.5:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25: #imc >= 18.5 and imc < 25
    print(f'O seu IMC é {imc:.1f}')
    print('Você está no peso ideal!')
elif 25 <= imc < 30:#imc >= 25 and imc < 30
    print(f'O seu IMC é {imc:.1f}')
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:#imc >= 30 and imc < 40
    print(f'O seu IMC é {imc:.1f}')
    print('Você está com obesidade!')
else:
    print(f'O seu IMC é {imc:.1f}')
    print('Você está com obesidade mórbida!')