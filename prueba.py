from math import floor
import numpy as np
from sympy import *



def validar_resultados(lista, media, desviacion_tipica):
    repetir = False
    for numero in lista:
        if numero < media - 2 * desviacion_tipica or numero > media + 2 * desviacion_tipica:
            lista.remove(numero)
            repetir = True

    return lista, repetir


# Obtenemos la posición de la ultima_cifra_significativa
def ultima_cifra_significativa(numero):
    if numero > 1:
        n = 1
        while floor(numero) != 0:
            numero /= 10
            n -= 1

    elif floor(numero) == 0 and numero != 0:
        n = 0
        while floor(numero) == 0:
            numero *= 10
            n += 1

    else:
        n = 0

    return n


def medidas_directas_error(lista, error_inicial = 0, resolucion = 0):
    # Calculamos la media y la desviacion típica.
    # He utilizado numpy aunque existen más modulos que nos proporcionan estas funciones.
    # Se pueden crear funciones para la media y desviación de manera muy sencilla.
    # Importo numpy para agilicidar el desarrollo del ejercicio
    media = np.mean(lista)
    desviacion_tipica = np.std(lista)

    # Validamos que si todos los datos que tenemos son validos
    # En caso de que no lo fueran los eliminamos y volvemos a hacer todo el procedimiento mediante recursividad
    lista, repetir = validar_resultados(lista, media, desviacion_tipica)
    if repetir:
        media, error_total = medidas_directas_error(lista, error_inicial, resolucion)

    if 'error_total' in locals():
        return media, error_total

    # Si tuvieramos nuestro aparato presentara algún error inicial debemos quitarselo a todas nuestras mediciones
    media -= error_inicial

    # Ahora calculamos el error cuadratico medio que en el caso de que tengamos un solo elemento sabemos que va a ser cero
    ECM = desviacion_tipica / np.sqrt(len(lista))

    # En caso de que no le pasemos la resolucion, la calculamos.
    # Nos va a quedar el decimal mas pequeño de todos los elementos de la lista
    if resolucion == 0:
        decimal = 0
        for numero in lista:
            if round(numero, decimal) != round(numero, decimal + 1):
                decimal = 0
                while round(numero, decimal) != round(numero, decimal + 1):
                    decimal += 1
        if decimal != 0:
            # Redondeamos para ajustar el sesgo producido entre int y float
            resolucion = round(pow(0.1, decimal), decimal)

    # Calculamos el error total
    error_total = ECM + resolucion

    # Redondeamos el error y la media a partir de la ultima cifra significativa
    # Criterio ASTM - E29
    cifra_significativa = ultima_cifra_significativa(error_total)
    error_total = round(error_total, cifra_significativa)
    media = round(media, cifra_significativa)

    return media, error_total

# De nuestra función despejamos la g, que es lo que queremos calcular
# g = 2*L/t^2

# Las medidas son una lista compuesta por la media y el error total
def medidas_indirectas_error(media_longitud, error_longitud, media_tiempo, error_tiempo):
    '''Esta función solo es válida para nuestra formula, en caso de tener otra tendríamos que buscar el error de otra manera
    ya sea de manera directa, usando logaritmos o funciones trigonométricas.
    Para ello necesitamos sacar las derivadas parciales de la formula y junto a la media calculada previamente sacar el error'''

    # Sacamos la media de g
    # g = 2*L/t^2
    g_sin_error = 2 * media_longitud / pow(media_tiempo, 2)
    print(g_sin_error)
    # Ajustamos por logaritmos para obtener el error y nos queda de la siguiente forma:
    error = g_sin_error*((error_longitud/media_longitud) - 2 * (error_tiempo / media_tiempo))

    # Valor absoulto del error
    if error < 0:
        error *= -1

    # Redondeamos por el criterio anteriormente usado
    cifra_significativa = ultima_cifra_significativa(error)
    error_final = round(error, cifra_significativa)
    g = round(g_sin_error, cifra_significativa)

    return g, error_final



