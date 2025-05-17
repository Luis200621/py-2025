#Guia de tipos de datos en python 

edad = 18
estatura = 1.80 
peso = 70
complejo = 2 + 9j 
complejo2 = (1, 4)

print(complejo)
print(complejo2)

imc = peso / (estatura ** 2)
print(f"Su IMC es: {imc: .4f}")
print("Su IMC es: {:.2f}".format (imc)) 
print(round(imc, 2))

print(float(edad))

carrera = 'Ingenieria Civil en Informatica'
asignatura = "programacion"
descripcion = '''Esta es una asignatura de primer semestere'''

print(carrera[0])

print("hola" * 4)

print(asignatura[0:6])
print(descripcion.split())
v = [1, 2, 3, 4, 5]
print(v[0])