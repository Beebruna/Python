'''
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ele.
'''

n = input('Digite algo: ')

print('O tipo é: ', type(n))
#print(f'O tipo é: {type(n)}')
print('É númerico? ', n.isnumeric())
#print(f'É numérico? {n.isnumeric()}')
print('É decimal? ', n.isdecimal())
print('É dígito? ', n.isdigit())
print('É alfabético? ', n.isalpha())
print('É alfanumério? ', n.isalnum())
print('É ASCII?', n.isascii())
print('É identificador? ', n.isidentifier())
print('Tudo está em maiúsculo? ', n.isupper())
print('Tudo está em minúsculo? ', n.islower())
print('Está capitalizado? ', n.istitle())
print('Só tem espaços? ', n.isspace())
print('É imprimível? ', n.isprintable())

#n é um objeto
