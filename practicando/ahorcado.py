import random 

def ahorcado():
    palabras = ["murciélago", "hipopótamo", "zarpar", "crisálida", "quimera", "tornado"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = set()
    letras_erradas = set()
    intentos_restantes = 6 


    print("🎮 Bienvenido al juego del Ahorcado 🎮")
    print("_" * len(palabra_secreta))

    while intentos_restantes > 0:
        #mostrar porgreso
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("palabra: ", " ". join(progreso))


        #entrada del usuario 
        intento = input("Adivina una letra: ").lower()
        
        
        #validaciones 
        if not intento.isalpha() or len(intento) != 1:
            print("⚠️ Ingresar solo una letra valida ⚠️")
            continue 

        if intento in letras_adivinadas or intento in letras_erradas:
            print("⚠️ Ya intestaste con está letra.")
            continue

        if intento in palabra_secreta:
            letras_adivinadas.add(intento)
            print("✅ ¡Bien! La letra está en la palabra")

        else:
            letras_erradas.add(intento)
            intentos_restantes -= 1
            print(f"❌ La letra no está. te quedan {intentos_restantes} intentos.")


        #verificar si ganó
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"🎉 ¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break

    else:
        print(f"☠️ ¡Perdiste! la palabra era: {palabra_secreta}")

        
#ejecutar el juego
ahorcado()




