# Tic tac toe Min Max con Poda Alfa Beta
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
            return fila[0]

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != '   ':
            return tablero[0][columna]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '   ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '   ':
        return tablero[0][2]
    
    if all(all(celda != '   ' for celda in fila) for fila in tablero):
        return 'Empate'

    return None 

def verificarGanador(tablero):
    ganador = hay_ganador(tablero)
    if ganador == " X ":
        return -1
    elif ganador == " O ":
        return 1
    else:
        return 0

def alphaBeta(tablero, profundidad, alfa, beta, esMaximizador):
    if hay_ganador(tablero) is not None or profundidad == 0:
        return verificarGanador(tablero)
    
    if esMaximizador:
        max_val = -1000
        for i in range(3):
            for j in range(3):
                # Verificar si la celda esta vacia y si es asi se coloca la ficha para el jugador O
                if tablero[i][j] == '   ':
                    tablero[i][j] = " O "
                    # Se llama recursivamente minimax para el jugador minimizador
                    puntuacion = alphaBeta(tablero, profundidad-1, alfa, beta, not esMaximizador)
                    # Se deshace el movimiento
                    tablero[i][j] = '   '
                    
                    max_val = max(max_val, puntuacion)
                    alfa = max(alfa, puntuacion)
                    if beta <= alfa:
                        break
        
        return max_val
    else:
        min_val = 1000
        for i in range(3):
            for j in range(3):
                # Verificar si la celda esta vacia y si es asi se coloca la ficha del jugador X
                if tablero[i][j] == '   ':
                    tablero[i][j] = " X "
                    # Se llama recursivamente minimax para el jugador Maximizador
                    puntuacion = alphaBeta(tablero, profundidad-1, alfa, beta, not esMaximizador)
                    # Se deshace el movimiento
                    tablero[i][j] = '   '
                    min_val = min(min_val, puntuacion)
                    beta = min(beta, puntuacion)
                    if beta <= alfa:
                        break
        return min_val    

def encontrar_MejorMovimientoMin(tablero,turno, jugador):
    mejorPuntuacion = -10000
    mejor_movimiento = None
    
    for i in range(9):
        if tablero[i//3][i%3] == '   ':
            tablero[i//3][i%3] = " O "
            movimiento_puntuacion = alphaBeta(tablero, 10-turno, -1000, 1000, not jugador)
            tablero[i//3][i%3] = '   '
            
            if movimiento_puntuacion > mejorPuntuacion:
                mejorPuntuacion = movimiento_puntuacion
                mejor_movimiento = i
    
    return mejor_movimiento

def encontrar_MejorMovimientoMax(tablero,turno, jugador):
    mejorPuntuacion = 10000
    mejor_movimiento = None
    
    for i in range(9):
        if tablero[i//3][i%3] == '   ':
            tablero[i//3][i%3] = " X "
            movimiento_puntuacion = alphaBeta(tablero, 10-turno, -1000, 1000, not jugador)
            tablero[i//3][i%3] = '   '
            
            if movimiento_puntuacion < mejorPuntuacion:
                mejorPuntuacion = movimiento_puntuacion
                mejor_movimiento = i
    
    return mejor_movimiento

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
        impTablero(tablero)
        ganador = hay_ganador(tablero)
        # Verificar si hay un ganador
        if ganador  is not None:    
            
            if ganador == "Empate":
                print('¡Empate!')
            else:
                print("¡El jugador",ganador, f"ha ganado en el turno {turno-1}!")
            break

        

        if turno % 2 == 1:
            print(f'Turno {turno} del jugador humano')
            if turno > 1:
                puntuacion = alphaBeta(tablero, 10-turno, -1000, 1000, False)
                print(f'Puntuación: {puntuacion}')
                if puntuacion == -1:
                    print('¡Si juegas de forma perfecta ganaras!')
                elif puntuacion == 1:
                    print('¡La computadora ganará!')
                else:
                    print('!Si juegas de forma perfecta habra un empate!')
            
            eleccion = int(input('Ingrese la posición (0-8): '))
            if eleccion in posicionesOcupadas:
                print('Esta posicion ya esta ocupada. Elige otra.')
                continue
            else:
                if eleccion not in posicionesDisponibles:
                    print('Elige una posición válida.') 
                    continue
                posicionesOcupadas.append(eleccion)
                posicionesDisponibles.remove(eleccion)
                tablero[eleccion//3][eleccion%3] = " X "
                turno += 1
        else:
            print(f'Turno {turno} de la computadora')
            eleccion = encontrar_MejorMovimientoMin(tablero,turno,True)
            time.sleep(1)
            print(f'La computadora elige la posición {eleccion}')
            posicionesOcupadas.append(eleccion)
            posicionesDisponibles.remove(eleccion)
            tablero[eleccion//3][eleccion%3] = " O "
            turno += 1  


def computadoraVsComputadora():
    tablero = crearNuevoTablero()
    turno = 1

    impTablero(tablero)
    print("Computadora 1: X")
    print("Computadora 2: O")
    print("Computadora 1 comienza")
    
    while True:
        print('*'*20)
        impTablero(tablero)
        ganador = hay_ganador(tablero)
        # Verificar si hay un ganador
        if ganador  is not None:    
            
            if ganador == "Empate":
                print('¡Empate!')
            else:
                print("¡El jugador",ganador, f"ha ganado en el turno {turno-1}!")
            break

        if turno % 2 == 1:
            print(f'Turno {turno} de la computadora 1')
            eleccion = encontrar_MejorMovimientoMax(tablero,turno,False)
            time.sleep(1)
            print(f'La computadora 1 elige la posición {eleccion}')
            
            tablero[eleccion//3][eleccion%3] = " X "
            turno += 1
        else:
            print(f'Turno {turno} de la computadora 2')
            eleccion = encontrar_MejorMovimientoMin(tablero,turno,True)
            time.sleep(1)
            print(f'La computadora 2 elige la posición {eleccion}')
            tablero[eleccion//3][eleccion%3] = " O "
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

