from os import system
system("cls")

lista_nombres = ["Maria", "Juan", "Pedro", "Ana", "Luis", "Carlos", "Laura", "Sofia"]

def busqueda_binaria(lista_nombres: list, elemento: str) -> str:
    """
    Función que divide la lista en mitades iterativamente
    hasta encontrar el elemento buscado o hasta que la 
    lista tenga un solo elemento.
    
    Args:
    lista_nombres (list): Lista de strings
    elemento (str): Elemento a buscar en la lista
    
    Returns:
    Devuelve un el elemnto buscado si está en la lista
    """
    inicio = 0
    final = len(lista_nombres) - 1
    while inicio < final:
        medio = (inicio + final)//2
        if lista_nombres[medio] == elemento:
            return medio
        elif lista_nombres[medio] < elemento:
            inicio = medio + 1
        else:
            final = medio - 1
    return None

elemento = "Ana"
busqueda = busqueda_binaria(lista_nombres, elemento)
print(f"El elemento {elemento} se encuentra en la posición: {busqueda}")