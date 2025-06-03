# Ingresar el nombre del producto y su precio unitario
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

# Ingresar la cantidad en stock
cantidad = int(input("Ingrese la cantidad en stock: "))

# Calcular el valor total y mostrarlo con 2 decimales
valor_total = round(precio_unitario * cantidad, 2)

# Crear la variable booleana umbral
umbral = valor_total > 100000

# Imprimir los datos formateados en un solo print()
print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Valor Total: ${valor_total:.2f}, Umbral: {umbral}")