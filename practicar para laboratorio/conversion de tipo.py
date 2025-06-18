año_actual = 2025

año = int(input('Ingrese su año de nacimiento: '))
edad = int(input('Ingrese su edad: '))

edad_real = año_actual - año

if edad == edad_real:
    print('Los datos ingresados coinciden')

else:
    print('Los datos no coinciden') 
    print(f'Segun tu año de nacimiento tu edad real es {edad_real} años')