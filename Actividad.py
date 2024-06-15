def validar_lista_numeros(entrada):
    while True:
        try:
            # Intentamos convertir la entrada en una lista de enteros
            lista_numeros = list(map(int, entrada.split()))
            return lista_numeros
        except ValueError:
            # Si hay un error, pedimos al usuario que ingrese la lista nuevamente
            entrada = input("Entrada no válida. Por favor ingrese una lista de números enteros separados por espacios: ")

def clasificar_numeros(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def main():
    entrada = input("Ingrese una lista de números enteros separados por espacios: ")
    lista_numeros = validar_lista_numeros(entrada)
    pares, impares = clasificar_numeros(lista_numeros)
    
    print("Números pares:", pares)
    print("Números impares:", impares)

# Llamada a la función principal
if __name__ == "__main__":
    main()
