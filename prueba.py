import numpy as np


a = [1, 3, 4, 5, 6, 7]
b = [2]

print(a)
print(len(b))
print(round(8.34, 1))

def medidas_directas_error(lista, error_inicial = 0, resolucion = 0):
    if error_inicial != 0:
        for i in range(len(lista)):
            lista[i] = lista[i] - error_inicial

    media = np.mean(lista)
    desviacion_tipica = np.std(lista)
    ECM = desviacion_tipica / np.sqrt(len(lista))

    if resolucion == 0:
        decimal = 0
        for numero in lista:
            if round(numero, decimal) != round(numero, decimal+1):
                decimal = 0
                while round(numero, decimal) != round(numero, decimal):
                    decimal += 1

        return decimal

medidas_directas_error(print([1.34, 2, 4.2, 6.4859, 3.2]))

