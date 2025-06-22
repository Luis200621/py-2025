#Nombres de los integrantes: Luis Muñoz y Dayana Levicoy 

numero = int(input('Ingresa un número para saber su factorial: '))

resultado = 1 

while numero > 1: 
    resultado *= numero 
    numero -= 1
    print(f'El factorial es {resultado}')