

persona = {}
persona["nombre"] = input("Nombre: ")
persona["edad"] = input("Edad: ")
persona["ciudad"] = input("Ciudad: ")

print("\n--- Datos Ingresados ---")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
