'''
n = float(input('Digite um valor: '))
print(n)
'''

n = input('Digite algo: ')
print(n.isnumeric())#O valor digitado é númerico?
'''função que diz se é possível converter o valor digitado em um número
com o tipo primitivo int antes dele
outros exemplos
isalpha() = é letra (apenas letras)? é alfabeto?
123 é string mas não é alpha
www é string e alpha
3a é string, alfanumérico, mas não é alpha

isalnum() = é alfanumérico?
oi é alfanumérico
3a é alfanumérico
7 é alfanumérico
"espaço" não é alfanumérico

isupper() = há apenas letras maiúsculas?
islower() = há apenas letras minúsculas?
isprintable() = pode ser impresso?
isspace() = é espaço?
etc.
são métodos de teste de tipos

valores retornados apenas pela função input() são sempre
do tipo string.
'''

