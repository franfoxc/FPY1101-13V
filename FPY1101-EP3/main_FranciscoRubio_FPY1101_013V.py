libros = []

def registrar_libro():
    Titulo = input("Ingrese nombre del libro: ")
    Autor = input("Ingrese nombre del autor: ")
    Año = input("Ingrese año de la publicación del libro: ")
    SKU = float(input("Ingrese el identificador del libro:"))

    libro = {
        'Titulo' : Titulo,
        'Autor' : Autor,
        'Año' : Año,
        'SKU' : SKU
    }

    libros.append(libro)
    print("Libro registrado con éxito.")

def Prestar_libro():
    for libro in libros:
        print(f"{libro['Titulo']} {libro['Autor']} {libro['Año']} {libro['SKU']}")

    def imprimir_préstamos():
        Prestar = ('ALAS DE HIERRO', 'LA SOMBREA DE LA SIRENA', 'DON QUIJOTE DE LA MANCHA.')
        print("Seleccione el nombre para imprimir los préstamos de los libros:")
        print("1. Todos")
        for i, Prestar in enumerate(Prestar, 2):
            print(f"{i}. {Prestar}")
        
        opción = int(input("Ingrese la opción: "))

        if opción == 1:
            listar_libros = libros
        else:
            Prestar_seleccionado = Prestar[opción - 2]
            listar_libros = [t for t in libros if t['Prestar'] == Prestar_seleccionado]

        nombre_archivo = "Planilla_libros.txt"
        with open(libros, 'w') as file:
            for libro in listar_libros:
                file.write(f"{libro['Titulo']} {libro['Autor']} {libro['Año']} {libro['SKU']}\n")
            
            print(f"Planilla de libros Prestados en el archivo {libros}. ")

            def main():
                while True:
                    print("Seleccione una opción:")
                    print("1. Regristar libro")
                    print("2. Prestar libro")
                    print("3. Listar todos los libros")
                    print("4. Imprimir reporte de préstamos")
                    print("5. Salir del Programa")

                    opción = int(input("Ingrese la opción: "))

                    if opción == 1:
                        registrar_libro()
                    elif opción == 2:
                        Prestar_libro()
                    elif opción == 3:
                        listar_libros()
                    elif opción == 4:
                        imprimir_préstamos()
                    elif opción == 5:
                        print("Saliendo del Programa.")
                        break
                    else:
                        print("Opción no válida. Intente Nuevamente.")

            if __name__ == "__main__":
                main()

        