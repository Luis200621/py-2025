n = int(input('Ingresar la cantidad de cubos que desea ver: '))

primer_impar = 1

for i in range(1, n + 1): 
    suma = 0
    secuencia = ''

    for j in range(i): 
        suma += primer_impar
        secuencia += (f'{primer_impar}')
        if j < i - 1: 
            secuencia += ' + '
        primer_impar += 2 

    print(f'{i}³ = {secuencia} = {suma}')