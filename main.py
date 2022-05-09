from planetas import planetas
from prueba import *

if __name__ == "__main__":
    n = int(input('¿Cuantas medidas se toman?\n'))

    longitudes = []
    print(f'Introduce {n} longitudes:')
    for i in range(n):
        temp = float(input(f'{i + 1} - '))
        longitudes.append(temp)

    tiempos = []
    print(f'Introduce {n} tiempos:')
    for i in range(n):
        temp = float(input(f'{i + 1} - '))
        tiempos.append(temp)

    error_inicial_longitud = float(input('¿Cual es el error inicial de la longitud?\n'))
    resolucion_longitud = float(input('Resolucion de longitud:\n'))
    error_inicial_tiempo = float(input('¿Cual es el error inicial del tiempo?\n'))
    resolucion_tiempo = float(input('Resolucion tiempo:\n'))

    media_longitud, error_longitud = medidas_directas_error(longitudes, error_inicial_longitud)
    media_tiempo, error_tiempo = medidas_directas_error(tiempos, error_inicial_tiempo)
    g, error_final = medidas_indirectas_error(media_longitud, error_longitud, media_tiempo, error_tiempo)

    print(f'Nuestra aproximacion de la gravedad es de {g} con un error de {error_final}')

    for planeta in planetas.keys():
        if planetas[planeta] < g + error_final and planetas[planeta] > g - error_final:
            print(f'Nos encontramos cerca del planeta {planeta}')












