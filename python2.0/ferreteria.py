#Definiendo variables
martillo = float(input("Ingrese el precio unitario del martillo: "))
martilloC = int(input("Ingrese la cantidad de martillos: "))

clavos = float(input("Ingrese el precio unitario de los clavos: "))
clavosC = int(input("Ingrese la cantidad de clavos: "))

serrucho = float(input("Ingrese el precio unitario del serrucho: "))
serruchoC = int(input("Ingrese la cantidad de serruchos: "))

tornillos = float(input("Ingrese el precio unitario de los tornillos: "))
tornillosC = int(input("Ingrese la cantidad de tornillos: "))

# Calcular subtotales
subtotal_martillo = round(martillo * martilloC, 2)
subtotal_clavos = round(clavos * clavosC, 2)
subtotal_serrucho = round(serrucho * serruchoC, 2)
subtotal_tornillos = round(tornillos * tornillosC, 2)

# Mostrar subtotales
print("\nSUBTOTALES:")
print(f"Martillo: ${subtotal_martillo}")
print(f"Clavos: ${subtotal_clavos}")
print(f"Serrucho: ${subtotal_serrucho}")
print(f"Tornillos: ${subtotal_tornillos}")

# Calcular suma total
total = subtotal_martillo + subtotal_clavos + subtotal_serrucho + subtotal_tornillos
print(f"\nTotal general: ${round(total, 2)}")

# Calcular valor máximo y mínimo
maximo = max(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)
minimo = min(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)
print(f"Valor máximo: ${maximo}")
print(f"Valor mínimo: ${minimo}")

# Calcular promedio del precio unitario
promedio_precios = round((martillo + clavos + serrucho + tornillos) / 4, 2)
print(f"Promedio precio unitario: ${promedio_precios}")

# Calcular IVA (19% del total)
iva = round(total * 0.19, 2)
print(f"IVA (19%): ${iva}")


