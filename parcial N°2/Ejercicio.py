#Letra A
veterinario = {
    101: {
        'nombre': 'Luna',
        'peso': 1.2 ,
        'edad': 3,
        'tamaño':30 
    },
    102: {
        'nombre': 'Michi',
        'peso': 0.8,
        'edad': 2,
        'tamaño': 25
    },
    103: {
        'nombre': 'Pepito',
        'peso': 2.5,
        'edad': 5,
        'tamaño': 35
    }
}

print(f'{veterinario} \n')

#letra B
for datos in veterinario.values() :
    peso = datos['peso']
    if peso < 1:
        datos['Clasificacion-peso'] = 'Bajo Peso'
    elif peso >= 1 and peso <=4:
        datos['Clasificacion-peso'] = 'Normal'
    else:
        datos['Clasificacion-peso'] = 'Sobre Peso'

print(f'{veterinario} \n')

#letra C
try :
    for datos in veterinario.values() :
        edad = datos['edad']
        if edad < 4:
            datos['Categoría-Etaria'] = 'Cachorro'
        elif edad >= 4 and edad <= 12:
            datos['Categoría-Etaria'] = 'Joven'
        else:
            datos['Categoría-Etaria'] = 'Adulto'
except:
    datos['Categoría-Etaria'] = 'Desconocida'

print(f'{veterinario} \n')

#Letra D
lista_pesos = [(ing, datos["peso"]) for ing, datos in veterinario.items()]
lista_pesos.sort(key=lambda x: x[1]) 

print(f'lista ordenada por su peso {lista_pesos} \n')

#Letra E

while True :
    try:
        numero_ingreso = int(input('N° de ingreso: '))
        nombre_gatito = input('nombre: ')
        peso_gatito = float(input('peso: '))
        edad_gatito = int(input('edad: '))
        tamaño_gatito = int(input('tamaño: '))
        
        veterinario[numero_ingreso] = {'nombre': nombre_gatito, 'peso': peso_gatito, 'edad': edad_gatito, 'tamaño': tamaño_gatito}

        seguir_agregando = input('¿Desea agregar otro gatito? (s/n): ')
        if seguir_agregando.lower() != 's':
            break
    except:
        print('Error al ingresar la informacion hacerca de el gatito\n')

print(f'{veterinario} \n')
#Letra F

numero_gatito = int(input('Porfavor ingrese el numero del gatito que desea modificar su estatura: '))

tamaño_nuevo = int(input('Porfavor ingresar Nuevo tamaño del gatito: '))

if numero_gatito in veterinario:
    veterinario[numero_gatito].update({'tamaño': tamaño_nuevo})
else:
    print('No se ha encontrado al gatito \n')

print(f'{veterinario} \n')

#Letra G
guardar_pesos = [datos['peso'] for datos in veterinario.values()]

promedio_pesos = sum(guardar_pesos) / len(guardar_pesos)
peso_maximo = max(guardar_pesos)
peso_minimo = min(guardar_pesos)

print(f'El promedio del peso de todos los gatitos es {promedio_pesos} \n, el peso maximo entre los gatitos es {peso_maximo} \n y el peso minimo entre los gatitos es {peso_minimo}')

print('Diccionario final ordenado por número de ingreso: ')
for ingreso in sorted(veterinario):
    print(ingreso, veterinario[ingreso])