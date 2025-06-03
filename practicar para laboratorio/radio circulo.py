pi = 3.1416 

circunferencia = float(input('Ingrese la circunferencia del circulo: '))

radio = circunferencia/ (2* pi) 

radio2 = round(radio ,3)

print('El radio del circulo es de: ', radio2)

area = pi * radio2**2
area2= round(area ,3)
print('El área del circulo es: ', area2)

