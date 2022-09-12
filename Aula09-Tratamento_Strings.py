
print('')
print('------------FATIAMENTO--------------')
frase = 'Curso em Vídeo'
print(frase[9])
print(frase[4:13])
print(frase[:3])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print('oi')
print(""""TEXTO GRANDES""")
frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.count('0',0,13))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print('-------------TRANSFORMAÇÃO--------------')
frase = 'Aprenda Python'
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print('-------------DIVISÃO---------------------')
frase ='Curso em Vídeo Python'
print(frase.split())
print('-'.join(frase))