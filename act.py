import random

# Función para crear el tablero vacío de tamaño n x n
def crearTablero(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

# Función para colocar el tesoro en una posición aleatoria del tablero
def colocarTesoro(tablero):
    n = len(tablero)
    filaTesoro = random.randint(0, n - 1)
    colTesoro = random.randint(0, n - 1)
    return filaTesoro, colTesoro  # Devolver las coordenadas del tesoro

# Función para validar que el tamaño del tablero es un número entero mayor que cero
def validarTamaño():
    while True:
        try:
            n = int(input("Ingresa el tamaño del tablero (N x N): "))
            if n > 0:
                return n
            else:
                print("El tamaño debe ser un número mayor que cero.")
        except ValueError:
            print("Debes ingresar un número entero válido.")

# Función para validar que las coordenadas ingresadas sean números enteros y estén dentro del rango
def validarCoordenadas(n):
    while True:
        try:
            fila = int(input(f"Ingrese la fila (0-{n-1}): "))
            columna = int(input(f"Ingrese la columna (0-{n-1}): "))
            if 0 <= fila < n and 0 <= columna < n:
                return fila, columna
            else:
                print(f"Las coordenadas deben estar entre 0 y {n-1}.")
        except ValueError:
            print("Debes ingresar números enteros válidos.")

# Función principal del juego
def jugarTesoroEscondido():
    print("¡Bienvenido al juego del Tesoro Escondido!")

    # Solicitar y validar el tamaño del tablero
    n = validarTamaño()

    # Crear el tablero y colocar el tesoro
    tablero = crearTablero(n)
    filaTesoro, colTesoro = colocarTesoro(tablero)

    intentos = 0
    encontrado = False

    while not encontrado:
        # Solicitar las coordenadas del jugador
        fila, columna = validarCoordenadas(n)
        intentos += 1

        # Verificar si el jugador ha encontrado el tesoro
        if fila == filaTesoro and columna == colTesoro:
            print(f"¡Felicitaciones! Has encontrado el tesoro en {intentos} intento(s).")
            encontrado = True
        else:
            print("Inténtalo de nuevo.")

# Iniciar el juego
if __name__ == "__main__":
    jugarTesoroEscondido()
