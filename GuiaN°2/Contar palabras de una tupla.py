#Nombres de los integrantes: Luis Muñoz y Dayana Levicoy 

texto = input('ingresar texto: ')

texto_separado = texto.split() 

if not texto_separado: 
    raise ValueError('El texto no puede estar vacío')

print(texto_separado)

contador = texto_separado.count(input('Ingrese la palabra que desea buscar: '))

print(contador)