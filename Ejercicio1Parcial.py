def contar_palabra(palabra, vector):
    if not vector:
        return 0
    else:
        if palabra == vector[0]:
            return 1 + contar_palabra(palabra, vector[1:])
        else:

            return contar_palabra(palabra, vector[1:])


# Ejemplo de uso
vector_palabras = ["hola", "mundo", "hola", "hola", "adios"]
palabra_buscada = "hola"

resultado = contar_palabra(palabra_buscada, vector_palabras)
print(
    f"La palabra '{palabra_buscada}' aparece {resultado} veces en el vector.")
