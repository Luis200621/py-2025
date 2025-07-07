# A) VARIABLES Y TIPOS DE DATOS
print("=== SISTEMA DE INVENTARIO ===")

categorias_unicas = set()
inventario = []

while True:
    print("\n--- Agregar producto ---")

    nombre = input("Nombre del producto: ")
    
    # F) EXCEPCIONES - Validar ingreso de números
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("⚠️ Error: Precio y cantidad deben ser números.")
        continue

    categoria = input("Categoría: ")

    # Mostrar tipos (parte A)
    print(f"(TIPOS) Nombre: {type(nombre)}, Precio: {type(precio)}, Cantidad: {type(cantidad)}, Categoría: {type(categoria)}")

    # B) TUPLA del producto
    tupla_producto = (nombre, precio, cantidad, categoria)
    print("Tupla producto:", tupla_producto)

    # B) SET para categorías únicas
    categorias_unicas.add(categoria)

    # C) DICCIONARIO del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    # Agregar al inventario (lista de diccionarios)
    inventario.append(producto)

    # G) Preguntar si quiere agregar más
    continuar = input("¿Deseas agregar otro producto? (s/n): ").lower()
    if continuar != 's':
        break

# G) BUCLE para mostrar todo el inventario
print("\n=== INVENTARIO COMPLETO ===")
for producto in inventario:
    print(f"\n📦 Producto: {producto['nombre']}")
    print(f"💲 Precio: ${producto['precio']}")
    print(f"📦 Cantidad: {producto['cantidad']}")
    print(f"🏷️ Categoría: {producto['categoria']}")

    # D) OPERADORES: Valor total en stock
    total = producto["precio"] * producto["cantidad"]
    print(f"📊 Valor total en stock: ${total:.2f}")

    # E) CONDICIONALES
    if producto["cantidad"] == 0:
        print("⚠️ Producto agotado.")
    elif producto["cantidad"] < 5:
        print("❗ Pocas unidades disponibles.")

    # E) MATCH CASE
    match producto["categoria"].lower():
        case "electrónica":
            print("🔌 Producto de tecnología.")
        case "ropa":
            print("👕 Prenda de vestir.")
        case "alimentos":
            print("🥫 Producto alimenticio.")
        case _:
            print("📦 Otra categoría.")

# B) Mostrar categorías únicas (SET)
print("\n📚 Categorías únicas registradas:", categorias_unicas)
