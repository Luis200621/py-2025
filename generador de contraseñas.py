import random
import string

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "⚠️ Debes seleccionar al menos un tipo de carácter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def menu_generador():
    print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS 🔐")

    try:
        longitud = int(input("Longitud de la contraseña: "))
        usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        usar_minus = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

        resultado = generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos)
        print(f"\n🔑 Contraseña generada: {resultado}")

    except ValueError:
        print("⚠️ Entrada inválida. Por favor, usa números donde corresponda.")

# Ejecutar el generador
menu_generador()
