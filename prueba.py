import numpy as np


a = [1, 3, 4, 5, 6, 7]
b = [2]
print(round(0.34))


def validar_resultados(lista, media, desviacion_tipica):
    repetir = False
    for numero in lista:
        if numero < media - 2 * desviacion_tipica or numero > media + 2 * desviacion_tipica:
            lista.remove(numero)
            repetir = True

    return lista, repetir

def medidas_directas_error(lista, error_inicial = 0, resolucion = 0):
    # Si tuvieramos nuestro aparato presentara algún error inicial debemos quitarselo a todas nuestras mediciones
    if error_inicial != 0:
        for i in range(len(lista)):
            lista[i] = lista[i] - error_inicial

    # Calculamos la media y la desviacion típica.
    # He utilizado numpy aunque existen más modulos que nos proporcionan estas funciones.
    # También se pueden crear de una manera muy sencilla
    media = np.mean(lista)
    desviacion_tipica = np.std(lista)

    # Validamos que si todos los datos que tenemos son validos
    # En caso de que no lo fueran los eliminamos y volvemos a hacer todo el procedimiento mediante recursividad
    lista, repetir = validar_resultados(lista, media, desviacion_tipica)
    if repetir:
        medidas_directas_error(lista, resolucion = resolucion)

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
            resolucion = round(pow(0.1, decimal), decimal)

    # Calculamos el error total
    error_total = ECM + resolucion

    return error_total


print(medidas_directas_error([1.34, 2, 4.2, 6.4859, 3.2]))

