"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re
presenta el día de la semana y cada fila a una de sus fábricas.

a)Crear una matriz con datos generados al azar para N fábricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique nin
guna. 
"""
import random

# Cargar la matriz con datos aleatorios de producción
def cargarMatriz(n):
    matriz = [] 
    for fila in range(n):
        filaIndividual = []
        for columna in range(6):  # 5 días de la semana (de lunes a viernes)
            value = random.randint(0, 150)  # Producción aleatoria entre 0 y 150 unidades
            filaIndividual.append(value)
        matriz.append(filaIndividual)
    return matriz

# Imprimir la matriz de producción
def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)

# Calcular la producción total de bicicletas por fábrica (fila)
def produccionPorFabrica(matriz):
    for i, fila in enumerate(matriz):
        total_produccion = sum(fila)  # Sumar la producción de toda la fila (una fábrica)
        print(f"Fábrica {i+1}: {total_produccion} bicicletas en la semana")

def mayorProduccion(matriz):
    dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    maximo = 0
    for i,fila in enumerate(matriz): #se usa enumerate cuando se quiere recorrer un iterable y se quiere obtener el indice como el valor
        actualMax = max(fila)
        if actualMax >= maximo :
            maximo = actualMax
            fabrica = i+1
            dia = dias[fila.index(actualMax)] #el indice de la fila busca ese valor y te devuelve el valor de indice donde se encuentra

    print(f" La fábrica {fabrica}: tiene el maximo en ventas de bicicletas: {maximo} el dia {dia}")

# Crear y mostrar la matriz
n = 6  # Número de fábricas
matriz = cargarMatriz(n)
print("Producción de bicicletas por día en cada fábrica:")
imprimirMatriz(matriz)

# Mostrar la producción total de cada fábrica
print("\nProducción total de bicicletas por fábrica durante la semana:")
produccionPorFabrica(matriz)

#
mayorProduccion(matriz)
