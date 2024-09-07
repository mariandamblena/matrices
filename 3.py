"""
 Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi
ta. Imprimir la matriz por pantalla.
"""
import random

# Función para imprimir la matriz
def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)

# Función para rellenar una matriz N x N con números aleatorios sin repeticiones
def rellenarMatriz(n):
    numeros = list(range(n**2))  # Generar una lista con números de 0 a N²-1
    random.shuffle(numeros)  # Barajar la lista para obtener números aleatorios sin repetición

    tablero = []  # Inicializar la matriz
    indice = 0  # Controlar el índice de la lista barajada
    for i in range(n):
        fila = []  
        for j in range(n):
            fila.append(numeros[indice])  # Asignar el número a la posición actual
            indice += 1  # Incrementar el índice
        tablero.append(fila)  # Agregar la fila a la matriz
    return tablero  

# Programa principal
n = int(input("Ingrese el orden de la matriz: "))
matriz = rellenarMatriz(n)
imprimirMatriz(matriz)
