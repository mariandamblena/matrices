"""
 Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar  las siguientes funciones y utilizarlas 
en un mismo programa:
 mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
se volverá a invocar luego de la misma con los estados actualizados.
 reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la 
sala en caso de estar disponible dicha butaca. La función devolverá True/False 
si logró o no reservar la butaca.
 cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
aleatorios para simular una sala con butacas ya reservadas.
 butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta
cas desocupadas hay en la sala.
 butacas_contiguas: Buscará la secuencia más larga de butacas libres conti
guas en una misma fila y devolverá las coordenadas de inicio de la misma. 


"""
import random

# Cargar la sala con valores aleatorios (True = ocupado, False = libre)
def cargar_sala(n, m):
    sala = []
    for fila in range(n):
        fila_individual = []
        for columna in range(m):
            # Simulamos que algunas butacas ya están reservadas
            fila_individual.append(random.choice([True, False]))
        sala.append(fila_individual)
    return sala

# Mostrar el estado de la sala (True = reservado, False = libre)
def mostrar_butacas(sala):
    print("Estado actual de las butacas (True = reservado, False = libre):")
    for fila in sala:
        print(fila)

# Reservar una butaca, actualizando la sala
def reservar(sala, fila, columna):
    if sala[fila][columna] == False:  # Si la butaca está libre
        sala[fila][columna] = True  # Reservar
        return True
    else:
        return False  # Si la butaca ya está ocupada

# Contar cuántas butacas libres hay en total
def butacas_libres(sala):
    libres = 0
    for fila in sala:
        libres += fila.count(False)  # Contar las butacas libres (False)
    return libres

# Buscar la secuencia más larga de butacas libres contiguas en una fila
def butacas_contiguas(sala):
    max_contiguas = 0
    inicio_contiguas = (-1, -1)  # Coordenadas de inicio de la secuencia más larga

    for i, fila in enumerate(sala):
        contiguas = 0
        inicio_temp = -1
        for j, butaca in enumerate(fila):
            if not butaca:  # Si la butaca está libre
                if contiguas == 0:
                    inicio_temp = j
                contiguas += 1
            else:
                if contiguas > max_contiguas:
                    max_contiguas = contiguas
                    inicio_contiguas = (i, inicio_temp)
                contiguas = 0

        # Revisar al final de la fila si la secuencia más larga es al final
        if contiguas > max_contiguas:
            max_contiguas = contiguas
            inicio_contiguas = (i, inicio_temp)

    return inicio_contiguas, max_contiguas

# Programa principal
n = 5  # Número de filas
m = 6  # Número de butacas por fila

# Cargar la sala con valores aleatorios
sala = cargar_sala(n, m)

# Mostrar el estado inicial de las butacas
mostrar_butacas(sala)

# Reservar una butaca
fila = int(input("Ingrese la fila para reservar (0-4): "))
columna = int(input("Ingrese la columna para reservar (0-5): "))
if reservar(sala, fila, columna):
    print("Butaca reservada con éxito.")
else:
    print("La butaca ya está ocupada.")

# Mostrar el estado actualizado de las butacas
mostrar_butacas(sala)

# Mostrar cuántas butacas libres hay en total
libres = butacas_libres(sala)
print(f"Hay {libres} butacas libres")
