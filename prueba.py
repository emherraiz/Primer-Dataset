from math import ceil, floor
import numpy as np


a = [1, 3, 4, 5, 6, 7]
b = [2]
print(6.4 % 2)

def par_true(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def validar_resultados(lista, media, desviacion_tipica):
    repetir = False
    for numero in lista:
        if numero < media - 2 * desviacion_tipica or numero > media + 2 * desviacion_tipica:
            lista.remove(numero)
            repetir = True

    return lista, repetir

# Criterio ASTM - E29, se podrían utilizar criterios más faciles
def cifra_significativa(media, error_total):
    if error_total < 1:
        decimal = 0
        redondeo = error_total
        while floor(redondeo) == 0:
            redondeo *= 10
            decimal += 1

        redondeo *= 10

        if (redondeo*10) % 5 == 0:
            if par_true(redondeo):
                redondeo = ceil(redondeo)
            else:
                redondeo = floor(redondeo)

print(cifra_significativa)



def medidas_directas_error(lista, error_inicial = 0, resolucion = 0):
    # Si tuvieramos nuestro aparato presentara algún error inicial debemos quitarselo a todas nuestras mediciones
    if error_inicial != 0:
        for i in range(len(lista)):
            lista[i] = lista[i] - error_inicial

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
            # Redondeamos para ajustar el sesgo producido entre int y float
            resolucion = round(pow(0.1, decimal), decimal)

    # Calculamos el error total
    error_total = ECM + resolucion

    return error_total


print(medidas_directas_error([1.34, 2, 4.2, 6.4859, 3.2]))

