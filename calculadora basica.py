def sumar (a, b):
    return a+b 

def restar (a, b):
    return a-b

def  multiplicar (a,b):
    return a*b

def dividir (a,b):
    if b != 0:
        return a/b 
    else:
        return "Error: división por cero."
    

print ("Calculadora Básica")

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

operacion = input("Elige la operacion que desea realizar (+, -, *, /): ")


if operacion == "+":
    print("Resultado:", sumar(a, b))

elif operacion == "-":
    print("Resultado:", restar(a, b))

elif operacion == "*":
    print("Resultado:", multiplicar(a, b))

elif operacion == "/": 
    print("Resultado:", dividir(a, b))
else:
    print("Operacion no valida")
   