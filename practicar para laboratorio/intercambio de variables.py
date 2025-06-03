# Valores originales
a = 5
b = 10

print("Antes del intercambio:")
print("a =", a)
print("b =", b)

# Intercambio usando una variable temporal
temp = a
a = b
b = temp

print("Después del intercambio:")
print("a =", a)
print("b =", b)


#ahora sin temp 
print('ahora sin temp')
# Valores originales
a = 5
b = 10

print("Antes del intercambio:")
print("a =", a)
print("b =", b)

# Intercambio directo en una línea
a, b = b, a

print("Después del intercambio:")
print("a =", a)
print("b =", b)
