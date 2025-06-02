#Ingresando variable celsius
gradosC = float(input('Ingrese los grados en Celsius: '))

#Calculando grados Celsius a Fahrenheit
print("Transformando el grado Celsius a Fahrenheit")
gradosF = 9/5 * gradosC +32 
print(round(gradosF ,2))

#Calculando grados fahrenheit a kelvin
print('Ahora lo transformaremos a Kelvin')
gradosK = (gradosF -32) * 5/9 + 273.15 
print(gradosK)

