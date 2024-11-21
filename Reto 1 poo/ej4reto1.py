# Función que retorna la mayor suma de dos números consecutivos de una lista.
def mayor_suma_consecutivos(lista_de_numeros):
    # Inicializa la mayor suma con la suma de los dos primeros números de la lista.
    mayor_suma = lista_de_numeros[0] + lista_de_numeros[1]
    # Itera desde el segundo elemento hasta el penúltimo.
    for i in range(1, len(lista_de_numeros) - 1):
        suma_actual = lista_de_numeros[i] + lista_de_numeros[i + 1]
        if suma_actual > mayor_suma: # Si la nueva suma es mayor que la "mayor suma"
            mayor_suma = suma_actual # La "mayor suma" se convertirá en la suma actual.
    return mayor_suma # Y retorna la mayor suma de las iteraciones.
# La lista de números:
if __name__ == "__main__":
    numeros = [14, 9, 21, 3, 2, 36]
    resultado = mayor_suma_consecutivos(numeros)
    # Imprime la mayor suma consecutiva.
    print(f"El resultado de la mayor suma consecutiva es: {resultado}")
