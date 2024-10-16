from os import system
system("cls")

#lista = 0
lista = [0]*5

def validar_lista(lista: list) -> list:
    """Valida si el elemento es una lista
    Args:
    lista(list): Es el elemento a verificar si es una lista
    """
    if type(lista) != list:
        return None
    return lista

def agregar_lista(lista: list) -> list:
    """Agrega elementos a la lista.

    Args:
    lista (list): Lista a la que se agrega elementos.
    elemento (any): Elemento que se va agregar a la lista.

    Returns:
    list: Lista con los elementos agregados.
    """
    cargar = "s"
    while cargar == "s":
        posicion = int(input("Ingrese posición de la lista: "))
        while posicion < 0 or posicion > len(lista):
            print("Posición inválida. Intente nuevamente.")
            posicion = int(input("Ingrese posición de la lista: "))
        
        elemento = int(input("Ingrese elemento a agregar: "))
        lista[posicion] = elemento

        cargar = input("¿Desea cargar otro elemento?(s/n): ")
        while cargar != "s" and cargar != "n":
            print("Opción inválida. Debe ingresar's' o 'n'.")
            cargar = input("¿Desea cargar otro elemento?(s/n): ")
        
    return lista

validar = validar_lista(lista)
if validar is not None:
    lista_cargada = agregar_lista(lista)
    print(lista_cargada)
else:
    print("La función debe recibir una lista")

