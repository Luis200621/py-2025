
#letra A
clima_chiloe = {
    5700000: {
        'Ciudad': 'Castro',
        'Temperatura': 11.8,
        'Precipitación': 2000
    },
    5770000: {
        'Ciudad': 'Chonchi',
        'Temperatura': 8.3,
        'Precipitación': 2800
    },
    5790000: {
        'Ciudad': 'Quellón',
        'Temperatura': 10.2,
        'Precipitación': 2950
    }
}

print(clima_chiloe)
#Letra B
# Castro
try:
    temperatura = clima_chiloe[5700000]['Temperatura']
    if temperatura < 10:
        clima_chiloe[5700000]['Clima'] = 'Frío'
    elif temperatura <= 15:
        clima_chiloe[5700000]['Clima'] = 'Templado'
    else:
        clima_chiloe[5700000]['Clima'] = 'Cálido'
except:
    clima_chiloe[5700000]['Clima'] = 'Desconocida'

# Chonchi
try:
    temperatura = clima_chiloe[5770000]['Temperatura']
    if temperatura < 10:
        clima_chiloe[5770000]['Clima'] = 'Frío'
    elif temperatura <= 15:
        clima_chiloe[5770000]['Clima'] = 'Templado'
    else:
        clima_chiloe[5770000]['Clima'] = 'Cálido'
except:
    clima_chiloe[5770000]['Clima'] = 'Desconocida'

# Quellón
try:
    temperatura = clima_chiloe[5790000]['Temperatura']
    if temperatura < 10:
        clima_chiloe[5790000]['Clima'] = 'Frío'
    elif temperatura <= 15:
        clima_chiloe[5790000]['Clima'] = 'Templado'
    else:
        clima_chiloe[5790000]['Clima'] = 'Cálido'
except:
    clima_chiloe[5790000]['Clima'] = 'Desconocida'

#Letra C

clima_chiloe[5700000]['Meses Más Lluviosos'] = []
clima_chiloe[5700000]['Meses Más Lluviosos'].append('Mayo')  
clima_chiloe[5700000]['Meses Más Lluviosos'].append('Junio')
clima_chiloe[5700000]['Meses Más Lluviosos'].append('Julio')

clima_chiloe[5700000]['Meses Más Lluviosos'].pop(1)

#Letra D
clima_chiloe[5770000]['Ciudad'] = 'Ciudad de los Tres Pisos'

#letra E 

Precipitación_castro = clima_chiloe[5700000]['Precipitación']
Precipitación_chonchi = clima_chiloe[5770000]['Precipitación']
Precipitación_quellón = clima_chiloe[5790000]['Precipitación']


lluvias = [Precipitación_castro + Precipitación_chonchi + Precipitación_quellón]

Precipitación = [clima_chiloe[5700000]['Precipitación'], clima_chiloe[5770000]['Precipitación'], clima_chiloe[5790000]['Precipitación']]

prec_max = max(Precipitación)
prec_min = min(Precipitación)
indice_max = Precipitación.index(prec_max)

print(f'\nLa suma total de las precipitaciónes es {lluvias}, la precipitación más pequeña es {prec_min} y la más grande es {prec_max} ademas el lugar de está es el {indice_max}\n')

#Letra F
print(clima_chiloe)

print('  \n')
#Letra G
lista_tuplas = list(clima_chiloe.items())

print(lista_tuplas)