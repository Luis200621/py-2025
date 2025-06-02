frase = str(input('Ingresar una frase de maximo 30 caracteres: ')) [ :30]

fraseMax = frase.upper() 
fraseMin = frase.lower()

print(fraseMax)
print(fraseMin)

print('La letra a aparece: ', frase.count('a'))
print('La letra A aparece: ', frase.count('A'))

print('La longitud de la palabra es de: ', len(frase))
