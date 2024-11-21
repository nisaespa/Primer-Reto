# Función para verificar si el número es primo.
def primo(numero):
    if numero <= 1: # Se descartan los números menores o iguales a 1.
        return False # Cuando retornamos falso es que no es primo.
    for i in range(2, int(numero**0.5) + 1): # Itera desde 2 hasta la raiz del número + 1.
        if numero % i == 0: # Si es divisible.
            return False # Cuando retornamos falso es que no es primo.
    return True # Cuando retornamos verdadero es que es primo.
# Se pide un número al usuario.
if __name__ == "__main__":
    numero = int(input("Ingresa un número entero para verificar si es primo: "))
    # Si es verdadero entonces se imprime que es primo.
    if primo(numero):
        print(f"El número {numero} es primo.")
    # Si no entonces se imprime que no es primo.
    else:
        print(f"El número {numero} no es primo.")
