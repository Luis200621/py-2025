#Nombres de los integrantes: Luis Muñoz y Dayana Levicoy 

tablero = {
    "a8": 'TorreN', 
    "b8": 'CaballoN', 
    "c8": 'AlfilN', 
    "d8": 'ReinaN', 
    "e8": 'ReyN', 
    "f8": 'AlfilN', 
    "g8": 'CaballoN', 
    "h8": 'TorreN',
    "a7": 'PeonN', 
    "b7": 'PeonN', 
    "c7": 'PeonN', 
    "d7": 'PeonN', 
    "e7": 'PeonN',
    "f7": 'PeonN', 
    "g7": 'PeonN', 
    "h7": 'PeonN',
    "a2": 'PeonB', 
    "b2": 'PeonB', 
    "c2": 'PeonB', 
    "d2": 'PeonB', 
    "e2": 'PeonB', 
    "f2": 'PeonB', 
    "g2": 'PeonB', 
    "h2": 'PeonB',
    "a1": 'TorreB', 
    "b1": 'CaballoB', 
    "c1": 'AlfilB', 
    "d1": 'ReinaB', 
    "e1": 'ReyB', 
    "f1": 'AlfilB', 
    "g1": 'CaballoB', 
    "h1": 'TorreB'
}

simbolos = {
    "TorreB": 'R', 
    "CaballoB": 'N', 
    "AlfilB": 'B', 
    "ReinaB": 'Q', 
    "ReyB": 'K', 
    "PeonB": 'P',
    "TorreN": 'r', 
    "CaballoN": 'n', 
    "AlfilN": 'b', 
    "ReinaN": 'q', 
    "ReyN": 'k', 
    "PeonN": 'p'
}

letra_a_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
num_a_letra = {v: k for k, v in letra_a_num.items()}

capturadas_b = [] 
capturadas_n = []  

turno = 'B'

while True:
    columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    filas = list(range(8, 0, -1))

    print('\n  a b c d e f g h')
    for f in filas:
        print(f, end=' ')
        for c in columnas:
            pos = c + str(f)
            if pos in tablero:
                print(simbolos[tablero[pos]], end=' ')
            else:
                print('.', end=' ')
        print(f)
    print(' a b c d e f g h')

    print('\nCapturadas por Blancas:', ' '.join([simbolos[p] for p in capturadas_b]))
    print('Capturadas por Negras :', ' '.join([simbolos[p] for p in capturadas_n]))

    print(f'\nTurno de {"Blancas" if turno == "B" else "Negras"}')
    origen = input('¿Que piesa desea mover?, ejemplo: e2 (o desea salir del juego): ')
    if origen == 'salir':
        break
    if origen not in tablero:
        print('No hay pieza en esa posición.')
        continue
    if tablero[origen][-1] != turno:
        print('Esa no es tu pieza.')
        continue

    destino = input('¿A que pocision del tablero desea mover?, ejemplo: e4 (o desea salir del juego): ')
    if destino == 'salir':
        break

    pieza = tablero[origen]
    tipo = pieza[:-1]
    color = pieza[-1]

    x1, y1 = letra_a_num[origen[0]], int(origen[1])
    x2, y2 = letra_a_num.get(destino[0], -1), int(destino[1]) if len(destino) == 2 else -1
    dx, dy = x2 - x1, y2 - y1

    mover = False
    ruta_limpia = True

    if tipo == 'Peon':
        dir = 1 if color == 'B' else -1
        fila_ini = 2 if color == 'B' else 7
        if dx == 0:
            if dy == dir and destino not in tablero:
                mover = True
            elif y1 == fila_ini and dy == 2*dir and destino not in tablero and (origen[0]+str(y1+dir)) not in tablero:
                mover = True
        elif abs(dx) == 1 and dy == dir and destino in tablero and tablero[destino][-1] != color:
            mover = True

    elif tipo == 'Torre':
        if dx == 0 or dy == 0:
            mover = True
            paso_x = (dx > 0) - (dx < 0)
            paso_y = (dy > 0) - (dy < 0)
            i, j = x1 + paso_x, y1 + paso_y
            while (i, j) != (x2, y2):
                pos = num_a_letra[i] + str(j)
                if pos in tablero:
                    ruta_limpia = False
                    break
                i += paso_x
                j += paso_y

    elif tipo == 'Alfil':
        if abs(dx) == abs(dy):
            mover = True
            paso_x = (dx > 0) - (dx < 0)
            paso_y = (dy > 0) - (dy < 0)
            i, j = x1 + paso_x, y1 + paso_y
            while (i, j) != (x2, y2):
                pos = num_a_letra[i] + str(j)
                if pos in tablero:
                    ruta_limpia = False
                    break
                i += paso_x
                j += paso_y

    elif tipo == 'Reina':
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):
            mover = True
            paso_x = (dx > 0) - (dx < 0)
            paso_y = (dy > 0) - (dy < 0)
            i, j = x1 + paso_x, y1 + paso_y
            while (i, j) != (x2, y2):
                pos = num_a_letra[i] + str(j)
                if pos in tablero:
                    ruta_limpia = False
                    break
                i += paso_x
                j += paso_y

    elif tipo == 'Caballo':
        if (abs(dx), abs(dy)) in [(1, 2), (2, 1)]:
            mover = True

    elif tipo == 'Rey':
        if abs(dx) <= 1 and abs(dy) <= 1:
            mover = True

    if not mover or not (0 <= x2 <= 7 and 1 <= y2 <= 8):
        print('Movimiento no valido.')
        continue
    if not ruta_limpia:
        print(' Hay una pieza en el camino.')
        continue
    if destino in tablero and tablero[destino][-1] == color:
        print(' No puedes capturar tu propia pieza.')
        continue

    if destino in tablero:
        capturada = tablero[destino]
        if color == 'B':
            capturadas_b.append(capturada)
        else:
            capturadas_n.append(capturada)
        print(f' Capturó a {capturada} en {destino}')
    tablero[destino] = pieza
    del tablero[origen]

    turno = 'N' if turno == 'B' else 'B' 
