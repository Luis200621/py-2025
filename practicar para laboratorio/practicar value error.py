while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print(f"Tienes {edad} años.")
        break  # Sale del bucle si no hubo error
    except ValueError:
        print("⚠️ Error: Debes ingresar un número entero. Intenta otra vez.")
