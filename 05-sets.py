#CREANDO SETS
colores = {'azul', 'rojo', 'azul', 'verde'}
colorcitos = {'azul', 'naranjo'}

#IMPRIMIENDO EL SET COLORES 
print(colores)

#AGREGANDO UN NUEVO ELEMENTO AL SET (MÉTODO ADD)
colores.add('blanco')
print(colores)

#ELIMINANDO UN ELEMENTO DEL SET
colores.discard('blanco')
print(colores)

#APLICANDO EL METODO DIFFERENCE 
diferencia = colores.difference(colorcitos)
print(diferencia)