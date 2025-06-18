#condicionales
edad = 19

if edad >= 18:
    print('Eres mayor de edad')

#Indentar
edad = 19

if edad >= 18:
    print('Eres mayor de edad')
print('Este print esta fuera del if')

#Else
edad = 19

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

#Elif
edad = 66

if edad >= 18 and edad < 65:
    print('Eres mayor de edad')
elif edad >= 65:
    print('Eres un adulto mayor')
else:
    print('Eres menor de edad')

#Operador terniario
edad = 19
print("Usted puede votar" if edad >= 18 else "Usted no puede votar")