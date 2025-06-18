#excepciones
print("====== MENÚ ======")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")

opcion = input("Por favor, elige una opción (1-3): ")

match opcion:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $5000")
    case "2":
        print("Has elegido Pizza. Precio: $7500")
    case "3":
        print("Has elegido Completo. Precio: $2500")
    case _:
        print("Opción no válida. Por favor, elige entre 1 y 3")

#patrones compuestos
x = [1, 2, 3]

match x:
    case [a, b, c]:
        print(f"Elementos de la Lista x: {a}, {b}, {c}")

datos = {'nombre': 'Victor', 'edad': 31}

match datos:
    case {'nombre': n, 'edad': e}:
        print(f"Nombre: {n}, Edad: {e}")

#Guards
valor = 6

match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un número Par")
    case x if x % 2 != 0:
        print(f"{valor} es un número Impar")