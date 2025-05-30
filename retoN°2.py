inventario = dict(
    manzana = (1500, 2000, 2500),
   
    platano = {2000, 2500, 2000},
    
    cereza =  (1000, 2000, 3000)
)

print(inventario)
tipos_frutas = ['Manzana', 'platano', 'cereza']
print(tipos_frutas)
precios_platano = (2000 + 2500 + 2000)/3

print(f"El promedio del platano es: {precios_platano: .3f}")