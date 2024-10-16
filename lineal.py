from os import system
system("cls")

def validar_lista(lista_nombres: list) -> list:
    """"
    Valida que el dato ingresado sea una lista.
    Si no lo es, imprime un mensaje de error y retorna None.
    
    Args:
    lista_nombres (list): Lista para validar
    """
    if type(lista_nombres) != list:
        print("El dato no es una lista")
        return None
    else:
        return lista_nombres
    
# Busqueda lineal
def buscar_lineal(lista_nombres: list, elemento: any) -> int:
    """
    Busca un elemento en la lista utilizando el metodo lineal.
    Si el elemento se encuentra, devuelve su posicion.
    Si no lo encuentra, devuelve None.
    
    Args:
    lista_nombres (list): Lista en la que buscar
    elemento (any): Elemento a buscar

    Returns:
    int: Posicion del elemento en la lista o None si no lo encuentra.
    """
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == elemento:
            return i
    return None

lista_nombres = ["Maria", "Juan", "Pedro", "Ana", "Luis", "Carlos", "Laura", "Sofia"]
valida = validar_lista(lista_nombres)
elemento = "Juan"

if valida is not None:
    buscar = buscar_lineal(lista_nombres, elemento)
    if buscar is not None:
        print(f"El elemento {elemento} se encuentra en la posicion {buscar} de la lista")
    else:
        print(f"El elemento {elemento} no se encuentra en la lista")
else:
    print("La lista no es valida")

