# Programación Orientada a Objetos - UNAL
## Primer Reto
### Explicación ejercicios:
1. Creé una función que se llama `operaciones`, que recibe dos números y el operador (+, -, *, /) del usuario, la función aplica condicionales dependiendo del operador, para hacer la operación con los dos números, e imprime el resultado.
```python
# Función que recibe dos números del usuario y realiza la operación que escoja el usuario.
def operaciones(operando1, operando2, operador):
    # Condicionales dependiendo de la operación.
    if operador == "+":
        return operando1 + operando2
    elif operador == "-":
        return operando1 - operando2
    elif operador == "*":
        return operando1 * operando2
    elif operador == "/":
        if operando2 != 0:
            return operando1 / operando2
        else:
            return "División por cero, operación no válida."
    else:
        return "Operación no válida."
# Ingreso de los dos núm eros del usuario y la operación que desee.
if __name__ == "__main__":
    numero1 = float(input("Escribe el primer operando: "))
    numero2 = float(input("Escribe el segundo operando: "))
    operador = input("Escribe el símbolo de la operación que quieres hacer (+, -, *, /): ")
    # Llamar a la función en una variable e imprimir resultado.
    resultado = operaciones(numero1, numero2, operador)
    print("El resultado es:", resultado)
```
2. Creé una función llamada `palindromo` que toma una palabra como entrada, para evitar problemas de mayúsculas y minúsculas, convertí la palabra a minúsculas usando el método `lower()`. Luego calculé la longitud de la palabra con `len()`, para verificar si es un palíndromo, implementé un bucle `for` que recorre los caracteres desde los extremos hacia el centro de la palabra. En cada iteración, comparé el carácter de la posición inicial con el correspondiente desde el final.
```python
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

```
3. Creé una función que verifica si un número es primo, el número se pide al usuario, utilicé un condional para descartar los numeros menores o iguales a 1. Luego utilizo un bucle `for` que recorre desde 2 hasta la raíz cuadrada del número, redondeada hacia abajo y aumentada en 1, comprobando si el número es divisible por alguno de esos valores; si encuentra un divisor retorna `False`, indicando que no es primo. Si pasa las pruebas retorna `True`, indicando que el número es primo.
```python
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
``` 
4. Creé una función que encuentra la suma más grande entre dos números consecutivos de una lista. Ya teniendo la lista calcula las primeras dos posiciones y las toma como la `mayor_suma`. Luego, revisa todas las parejas de números consecutivos, mediante un ciclo `for`, itera desde el segundo número hasta el penúltimo, calculando la suma de cada pareja . Si encuentra una suma mayor que la que tenía registrada, actualiza el valor de `mayor_suma`. Al finalizar el ciclo, imprime la `mayor_suma`.
```python
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
```
5. Creé una función que utiliza dos bucles `for` para comparar cada palabra de la lista con las que vienen después de ella, para cada par de palabras ordena sus letras y mira si son iguales, lo que indica que tienen las mismas letras. Se añaden a una lista vacía e imprime la lista con las palabras con letras iguales.
```python
# Función que devuelve las palabras de una lista que tengan las mismas letras.
def mismos_caracteres(lista):
    # Lista vacía para 
    vacia = []
    # Bucle anidado para comparar cada palabra con las demás.
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            # Comparar si las palabras tienen las mismas letras.
            if sorted(lista[i]) == sorted(lista[j]):
                # Añadir ambas palabras si aún no están en el la lista vacía.
                if lista[i] not in vacia:
                    vacia.append(lista[i])
                if lista[j] not in vacia:
                    vacia.append(lista[j])
    return vacia
if __name__ == "__main__":
    entrada = ["amor", "roma", "perro"]
    resultado = mismos_caracteres(entrada)
    print(resultado)
```
