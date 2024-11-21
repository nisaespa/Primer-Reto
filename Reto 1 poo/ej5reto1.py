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
