# Función que evalua si una palabra es un palíndromo.
def palindromo(palabra):
    palabra = palabra.lower()
    longitud = len(palabra)
    # Comparar los caracteres desde los extremos hacia el centro.
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    return True
# Solicitar una palabra al usuario y verificar si es un palíndromo.
if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    if palindromo(palabra):
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')
