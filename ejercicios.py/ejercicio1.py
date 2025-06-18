productos = ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch']
valor = [300, 800, 150 ,200]

stock = {
    'Smartphone' : 25,
    'Laptop' : 12,
    'Tablet' : 8,
    'Smartwatch' : 4

}

max_precio = max(valor)
min_precio = min(valor)

prod_max = productos[valor.index(max_precio)]
prod_min = productos[valor.index(min_precio)]

print(f'El articulo mas caro es {prod_max} con un valor de {max_precio}')
print(f'El articulo mas barato es {prod_min} con un valor de {min_precio}\n\n')

for prod, precio in zip(productos, valor):
    if precio < 200:
        categoria = 'Producto Economico'
    elif precio >=200 and precio <=500:
        categoria = 'Producto Estandar'
    else:
        categoria = 'Producto Premium'
    print(f'{prod}: ${precio} -> {categoria}')
print()

for prod,cantidad in stock.items(): 
    if cantidad < 10:
        print(f'{prod}: {cantidad} unidades')
