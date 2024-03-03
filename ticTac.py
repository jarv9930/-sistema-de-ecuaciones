
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

