"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
ción:
 a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
 c. Intercambiar dos filas, cuyos números se reciben como parámetro.
 d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
 e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
 f.
 Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
 g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
mero se recibe como parámetro.
 h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
 i.
 Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
 j.
 Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
"""
# Función para validar que el valor ingresado es un entero positivo
def intPositivo():
    num = input("Ingrese un número mayor que 0: \n")
    
    # Usar while para seguir pidiendo hasta que el número sea correcto
    while not num.isdigit() or int(num) <= 0:
        num = input("Valor ingresado incorrecto, ingrese un número mayor que 0: \n")
    
    return int(num)

# a. Función para cargar números enteros en una matriz de N x N
def cargarMatriz(n):
    matriz = [] 
    for fila in range(n):
        filaIndividual = []
        for columna in range(n):
            value = intPositivo()  # Ingresar los valores de la matriz desde teclado
            filaIndividual.append(value)
        matriz.append(filaIndividual)
    return matriz

# b. Función para ordenar en forma ascendente cada una de las filas de la matriz
def ordenarFilas(matriz):
    for fila in matriz:
        fila.sort()  # Ordenar cada fila de la matriz de manera ascendente
    return matriz

# c. Función para intercambiar dos filas
def intercambiarFilas(matriz, fila1, fila2):
    if fila1 < len(matriz) and fila2 < len(matriz):
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]  # Intercambiar filas
    return matriz

# d. Función para intercambiar dos columnas
def intercambiarColumnas(matriz, col1, col2):
    if col1 < len(matriz[0]) and col2 < len(matriz[0]):
        for fila in matriz:
            fila[col1], fila[col2] = fila[col2], fila[col1]  # Intercambiar columnas
    return matriz

# e. Función para trasponer la matriz sobre sí misma (intercambiar Aij por Aji)
def trasponerMatriz(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]  # Intercambio Aij por Aji
    return matriz

# f. Función para calcular el promedio de los elementos de una fila
def promedioFila(matriz, numFila):
    if 0 <= numFila < len(matriz):
        return sum(matriz[numFila]) / len(matriz[numFila])
    else:
        return None

# g. Función para calcular el porcentaje de elementos con valor impar en una columna
def porcentajeImparesColumna(matriz, numCol):
    if 0 <= numCol < len(matriz[0]):
        total = len(matriz)
        impares = sum(1 for fila in matriz if fila[numCol] % 2 != 0)  # Contar los impares
        return (impares / total) * 100
    else:
        return None

# h. Función para determinar si la matriz es simétrica con respecto a su diagonal principal
def esSimetricaDiagonalPrincipal(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:  # Verificar si Aij != Aji
                return False
    return True

# i. Función para determinar si la matriz es simétrica con respecto a su diagonal secundaria
def esSimetricaDiagonalSecundaria(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n - i - 1):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:  # Verificar simetría en diagonal secundaria
                return False
    return True

# j. Función para determinar qué columnas de la matriz son palíndromos
def columnasPalindromos(matriz):
    columnas_palindromos = []
    for col in range(len(matriz[0])):
        columna = [fila[col] for fila in matriz]
        if columna == columna[::-1]:  # Verificar si la columna es un palíndromo
            columnas_palindromos.append(col)
    return columnas_palindromos

# Función para imprimir la matriz
def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)

# Programa principal para verificar el funcionamiento
if __name__ == "__main__":
    n = intPositivo()  # Pedir el tamaño de la matriz N x N
    matriz = cargarMatriz(n)
    
    print("\nMatriz original:")
    imprimirMatriz(matriz)

    # b. Ordenar las filas de la matriz
    matriz = ordenarFilas(matriz)
    print("\nMatriz con filas ordenadas:")
    imprimirMatriz(matriz)
    
    # c. Intercambiar dos filas
    fila1 = int(input("\nIngrese el número de la primera fila a intercambiar (0 a N-1): "))
    fila2 = int(input("Ingrese el número de la segunda fila a intercambiar (0 a N-1): "))
    matriz = intercambiarFilas(matriz, fila1, fila2)
    print("\nMatriz después de intercambiar las filas:")
    imprimirMatriz(matriz)
    
    # d. Intercambiar dos columnas
    col1 = int(input("\nIngrese el número de la primera columna a intercambiar (0 a N-1): "))
    col2 = int(input("Ingrese el número de la segunda columna a intercambiar (0 a N-1): "))
    matriz = intercambiarColumnas(matriz, col1, col2)
    print("\nMatriz después de intercambiar las columnas:")
    imprimirMatriz(matriz)

    # e. Trasponer la matriz
    matriz = trasponerMatriz(matriz)
    print("\nMatriz traspuesta:")
    imprimirMatriz(matriz)
    
    # f. Calcular el promedio de una fila
    fila = int(input("\nIngrese el número de fila para calcular el promedio (0 a N-1): "))
    promedio = promedioFila(matriz, fila)
    if promedio is not None:
        print(f"El promedio de la fila {fila} es: {promedio}")
    else:
        print("Fila fuera de rango.")

    # g. Calcular el porcentaje de impares en una columna
    columna = int(input("\nIngrese el número de columna para calcular el porcentaje de impares (0 a N-1): "))
    porcentaje = porcentajeImparesColumna(matriz, columna)
    if porcentaje is not None:
        print(f"El porcentaje de impares en la columna {columna} es: {porcentaje:.2f}%")
    else:
        print("Columna fuera de rango.")
    
    # h. Verificar si la matriz es simétrica respecto a la diagonal principal
    if esSimetricaDiagonalPrincipal(matriz):
        print("\nLa matriz es simétrica respecto a la diagonal principal.")
    else:
        print("\nLa matriz no es simétrica respecto a la diagonal principal.")

    # i. Verificar si la matriz es simétrica respecto a la diagonal secundaria
    if esSimetricaDiagonalSecundaria(matriz):
        print("La matriz es simétrica respecto a la diagonal secundaria.")
    else:
        print("La matriz no es simétrica respecto a la diagonal secundaria.")

    # j. Determinar qué columnas son palíndromos
    columnas_palindromos = columnasPalindromos(matriz)
    if columnas_palindromos:
        print(f"\nLas siguientes columnas son palíndromos: {columnas_palindromos}")
    else:
        print("\nNo hay columnas palíndromos.")
