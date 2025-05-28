#CREANDO DICCIONARIO (SE AGREGAN DIFERENTES TIPOS DE DATOS ESTRUCTURADOS)
paciente = {
    'nombre': 'luis',
    'apellido': 'muñoz',
    'edad' : 18,
    'ciudad' : 'quellon',
    'consultas' : [14, 20, 40],
    'diagnostico' : ('resfrio')
}

# OTRA FORMA DE DECLARAR DICCIONARIO 
medico = dict(
    nombre = 'samuel',
    apellido = 'muñoz',
    edad = 18,
    especialidad = 'neurologo'
)

#IMPRESION DE DICCIONARIOS
print(paciente)
print(medico) 

#CONSULTANDO UN ELEMENTO A TRÁVEZ DE LA CLAVE DEL DICCIONARIO 
print(medico['nombre'])

#ELIMINANDO UNA CLAVE DEL DICCIONARIO (METODO DEL)
del(paciente['nombre'])
print(paciente)
