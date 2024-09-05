import random

# Función para validar que el valor ingresado es un entero positivo
def intPositivo():
    num = input("Ingrese un número mayor que 0: \n")
    
    # Usar while para seguir pidiendo hasta que el número sea correcto
    while not num.isdigit() or int(num) <= 0:
        num = input("Valor ingresado incorrecto, ingrese un número mayor que 0: \n")
    
    return int(num)

def crearTablero(n):
    tablero = []  
    for i in range(n):  
        fila = []  
        for j in range(n):  
            fila.append(' ')  
        tablero.append(fila)  
    return tablero  

# Función para colocar el tesoro en una posición aleatoria del tablero
def colocarTesoro(tablero):
    n = len(tablero)
    filaTesoro = random.randint(0, n - 1)
    colTesoro = random.randint(0, n - 1)
    return filaTesoro, colTesoro  

# Función para validar que las coordenadas ingresadas estén dentro del rango
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
            print("Tenes que ingresar números enteros válidos.")

# Función principal del juego
def jugarTesoroEscondido():
    print("¡Bienvenido al juego del Tesoro Escondido!")

    # Solicitar y validar el tamaño del tablero
    n = intPositivo()

    # Crear el tablero y colocar el tesoro
    tablero = crearTablero(n)
    filaTesoro, colTesoro = colocarTesoro(tablero)

    intentos = 0
    encontrado = False

    # Bucle para el juego, hasta que el jugador encuentre el tesoro
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

if __name__ == "__main__":
    jugarTesoroEscondido()

