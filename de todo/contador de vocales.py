texto = input ("ingresa una frase o palabra: ")

contador = 0


for letra in texto: 
    if letra.lower() in "aeiou":
        contador += 1
        print (f"La cantidad de vocales en el texto es: {contador}")