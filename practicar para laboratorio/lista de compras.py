productos = []

print('Ingrese 5 productos para tu lista de compras: ')

for i in range(5):
    producto = input(f'Producto *{i + 1}: ')
    productos.append(producto)

opcion = input('¿Quieres ver la lista ordenada alfabéticamente? (sí/no): ').strip().lower()

if opcion == 'Si' or opcion == 'si' or opcion == 'SI' or 'sI':
    print('Lista ordenada: ')
    print(sorted(productos))
else:
    print('Lista original: ')
    print(productos)