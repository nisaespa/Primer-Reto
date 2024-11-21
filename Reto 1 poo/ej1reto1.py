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