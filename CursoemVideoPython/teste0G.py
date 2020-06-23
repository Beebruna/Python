frase = 'Curso em Vídeo Python'

print(frase)

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))#o =! O
#Pega a frase, joga para maiúscula, e conta a quantidade de 'O"s
print(frase.upper().count('O'))
#frase é uma string,mas TUDO em pythn é um objeto, que através que podem ter seus métodos acessados pelo (.)

print(len(frase))
#Espaços são computados
frase = '   Curso em Vídeo Python   '
print(len(frase))
print(len(frase.strip()))

frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))# Não é definitivo!
print(frase)
frase = frase.replace('Python', 'Android')# É definitivo!
print(frase)
print(frase[0])
# >>> frase[0] = 'J' não é permitido!

print('Curso' in frase)
print(frase.find('Curso'))#'Curso' começa na posição 0
print(frase.find('Vídeo'))#'Vídeo' começa na posição 9
print(frase.find('vídeo'))#'vídeo" em minúsculo não existe
print(frase.lower().find('vídeo'))#Agora vídeo existe na frase toda em minúsculas

print(frase.split())
dividido = frase.split()
print(dividido[0])
#Pega o divido[2] e mostra a letra na posição 3
print(dividido[2][3])


#aspas duplas triplas para um imprimir um texto print("""texto""")
print("""\n\n\nTu es mon beau rêve réalisé
Tu es un conte de fée
Mon amour d'éternité
Mon plus bel été
Mon éternel printemps
Tu es simplement
Tout ce que je souhaitais""")
