# Tic tac toe Min Max
# Nava Izquierdo César
# Candia Navarro Iván
# Brandon Aldair Diaz Ortiz
# Flores Estopier Rodrigo
# Rodriguez Valle Josue Abraham
# 6CV2
import random, time

def impTablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end = "|")
        print("")
        print("-"*14)
    
        
def crearNuevoTablero():
    tablero = [["   " for _ in range(3)] for _ in range(3)]
    return tablero

# Función para verificar si hay un ganador
def hay_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != '   ':
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != '   ':
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '   ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '   ':
        return True

    return False     

def minimax(tablero, profundidad, esMaximizador):
    if hay_ganador(tablero):
        return -1 if esMaximizador else 1
    if profundidad == 0:
        return 0
    if esMaximizador:
        mejor = -1000
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '   ':
                    tablero[i][j] = " O "
                    mejor = max(mejor, minimax(tablero, profundidad-1, not esMaximizador))
                    tablero[i][j] = '   '
        return mejor
    else:
        mejor = 1000
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '   ':
                    tablero[i][j] = " X "
                    mejor = min(mejor, minimax(tablero, profundidad-1, not esMaximizador))
                    tablero[i][j] = '   '
        return mejor   

def jugarvsComputadora():
    tablero = crearNuevoTablero()
    turno = 1

    
            
    posicionesDisponibles = list(range(9))
    posicionesOcupadas = []
    impTablero(tablero)
    print("Jugador 1: X")
    print("Computadora: O")
    print("Jugador 1 comienza")
    
    while True:
        print('*'*20)
        # Turno del jugador
        print(f'Turno {turno} del jugador humano')
        if turno > 1:
            puntuacion = minimax(tablero, 10-turno, False)
            print(f'Puntuación: {puntuacion}')
            if puntuacion == -1:
                print('¡Si juegas de forma perfecta ganaras!')
            elif puntuacion == 1:
                print('¡Si la computadora juega de manera perfecta ganará!')
            else:
                print('!Si ambos juegan de forma perfecta el juego quedara en un empate!')

        eleccion = int(input('Ingrese la posición (0-8): '))
        
        if eleccion in posicionesOcupadas:
            print('Esta posicion ya esta ocupada. Elige otra.')
            
            continue
        else:
            if eleccion   not in posicionesDisponibles:
                print('Elige una posición válida.') 
                continue
            posicionesOcupadas.append(eleccion)
            posicionesDisponibles.remove(eleccion)
            tablero[eleccion//3][eleccion%3] = " X "
          
        impTablero(tablero)
        # Verificar si gano
        if hay_ganador(tablero):
            print(f'¡El jugador "X" ha ganado en el turno {turno}!')
            break
        # Verificar si hay un empate
        if turno == 9:
            print('¡Empate!')
            break
        
        turno += 1
        
        print(f'Turno {turno} de la computadora')
        if turno > 1:
            puntuacion = minimax(tablero, 10-turno, True)
            print(f'Puntuación: {puntuacion}')
            if puntuacion == -1:
                print('¡Si juegas de forma perfecta ganaras!')
            elif puntuacion == 1:
                print('¡Si la computadora juega de manera perfecta ganará!')
            else:
                print('!Si ambos juegan de forma perfecta el juego quedara en un empate!')
        time.sleep(2)
        # Turno de la computadora
        eleccion = random.choice(posicionesDisponibles)
        posicionesOcupadas.append(eleccion)
        posicionesDisponibles.remove(eleccion)
        tablero[eleccion//3][eleccion%3] = " O "
        impTablero(tablero)
        # Verificar si hay un ganador
        if hay_ganador(tablero):
            print(f'¡La computadora "O" ha ganado en el turno {turno}!')
            break
        # Verificar si hay un empate
        if turno == 9:
            print('¡Empate!')
            break
        turno += 1    

def computadoraVsComputadora():
    tablero = crearNuevoTablero()
    turno = 1
    posicionesDisponibles = list(range(9))
    posicionesOcupadas = []
    impTablero(tablero)
    print("Computadora 1: X")
    print("Computadora 2: O")
    print("Computadora 1 comienza")
    while True:
        print('*'*20)
        
        # Turno de la computadora 1
        print(f'Turno {turno} de la computadora 1')
        if turno > 1:
            puntuacion = minimax(tablero, 10-turno, False)
            print(f'Puntuación: {puntuacion}')
            if puntuacion == -1:
                print('¡Si la computadora 1 juega de forma perfecta ganara!')
            elif puntuacion == 1:
                print('¡Si la computadora 2 juega de manera perfecta ganará!')
            else:
                print('!Si ambos juegan de forma perfecta el juego quedara en un empate!')
        time.sleep(2)
        eleccion = random.choice(posicionesDisponibles)
        posicionesOcupadas.append(eleccion)
        posicionesDisponibles.remove(eleccion)
        tablero[eleccion//3][eleccion%3] = " X "
        impTablero(tablero)
        # Verificar si hay un ganador
        if hay_ganador(tablero):
            print(f'¡La computadora 1 "X" ha ganado en el turno {turno}!')
            break
        # Verificar si hay un empate
        if turno == 9:
            print('¡Empate!')
            break
        turno += 1
          
        # Turno de la computadora 2
        print(f'Turno {turno} de la computadora 2')
        if turno > 1:
            puntuacion = minimax(tablero, 10-turno, True)
            print(f'Puntuación: {puntuacion}')
            if puntuacion == -1:
                print('¡Si la computadora 1 juega de forma perfecta ganara!')
            elif puntuacion == 1:
                print('¡Si la computadora 2 juega de manera perfecta ganará!')
            else:
                print('!Si ambos juegan de forma perfecta el juego quedara en un empate!')
        time.sleep(2)
        eleccion = random.choice(posicionesDisponibles)
        posicionesOcupadas.append(eleccion)
        posicionesDisponibles.remove(eleccion)
        tablero[eleccion//3][eleccion%3] = " O "
        impTablero(tablero)
        # Verificar si hay un ganador
        if hay_ganador(tablero):
            print(f'¡La computadora 2 "O" ha ganado en el turno {turno}!')
            break
        # Verificar si hay un empate
        if turno == 9:
            print('¡Empate!')
            break
        turno += 1 
        
def menu():
    print("*********Tic Tac Toe*********")
    print("1. Jugar contra la computadora")
    print("2. Computadora vs Computadora")
    print("3. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion
                  

#jugarvsComputadora()
opcion = menu()
while opcion != 3:
    if opcion == 1:
        jugarvsComputadora()
    elif opcion == 2:
        computadoraVsComputadora()
    else:
        print("Opción inválida")
    opcion = menu()

