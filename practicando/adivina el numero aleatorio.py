import random 

def adivina_el_numero():
    numero_secreto = random.randint(1,100) 
    intentos = 0
    print("¡Adivina el número entre 1 y 100!")

    while True:
        try: 
            adivinanza = int(input("Ingresa tu número: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                break

        except ValueError:
            print("Por favor, ingresa un número Válido.")

#Ejecutar el juego
adivina_el_numero()
                


