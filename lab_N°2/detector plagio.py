texto =input('\nPorfavor ingresar el resumen de un texto Cientifico: ')

cumple = len(texto) <= 50
textoMayus= texto.upper()
textoMinus= texto.lower()

print('\nEl texto cumple con el limite de caracteres', cumple ) 

print('\nLa longitud total del texto es de ', len(texto), 'caracteres' )

print('\n',textoMayus)

print('\n',textoMinus)

print('\nLa cantidad de veces que aparece la letra e es: ', texto.count('e'))

print('\nLos primeros 15 caracteres del texto son: ', texto[ :15])

print('\nLos ultimos 15 caracteres del texto son: ', texto[-15: ])

palabras_con_comas = ",".join(texto.split())

print("Palabras unidas por comas:", palabras_con_comas)