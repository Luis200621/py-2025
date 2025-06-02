#Operaciones mixtas 
numeroE = int(input('Ingresar numero entero: '))
numeroF = float(input('Ingresar un numero decimal: '))
numeroC = complex(input('Ingrese un numero complejo (3 + 4j): '))

print('Calculando Potencia compleja: ')
resultadoP = numeroC**numeroE 
print(resultadoP)

print('Calculando Suma mixta: ')
resultadoS = numeroC + numeroF
print(resultadoS)

print('Producto Mixto: ')
resultadoM = numeroC * numeroE 
print(resultadoM)

print('Calculando Módulo de  Potencia Compleja: ')
resultadoMod = abs(resultadoP)
resultadoRealMod = round(resultadoMod ,3) 
print(resultadoRealMod)