from os import system
system("cls")

#lista = 1245
#valida la lista
#ordenar de manera ascendente


def validar_lista(lista: list) -> list:
    """Valida si el elemento es una lista
    Args:
    lista(list): Es el elemento a verficar si es una lista

    Returns:
    list: Devuelve una lista si se verifica sino devuelve None
    """
    if type(lista)!= list:
        #print("Error: La lista debe ser de tipo lista.")
        return None
    else:
        return lista
    
# Ordena en forma ascendente
def ordenar_lista(lista: list) -> list:
    """Ordena la lista en forma ascendente
    Aegs:
    lista (list): Lista a ordenar
    
    Returns:
    list: Devuelve la lista ordenada en forma 
    ascendente
    """
    lista_ordenada = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    lista_ordenada += lista
    return  lista_ordenada

# Ordenar en forma descendente
def ordenar_descendente(lista: list) -> list:
    """Ordena la lista en forma descendente
    Aegs:
    lista (list): Lista a ordenar
    
    Returns:
    list: Devuelve la lista ordenada en forma 
    descendente
    """
    lista_descendente = []
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    lista_descendente += lista
    return  lista_descendente

def buscar_lineal(lista: list, buscado: int)-> int:
    """Busca un elemento dentro de la lista, si lo
    encuentra retorna la posición y sino retorna None.

    Args:
        lista (list): Lista donde se busca el elemnto.
        buscado (int): Elemento a buscar en la lista.

    Returns:
        int: Posición del elemento buscado si lo encuentra,
        None si no lo encuentra.

    """
    contador = 0  # Contador de iteraciones
    for i in range(len(lista)):
        contador += 1  # Incrementar el contador en cada iteración
        if lista[i] == buscado:
            print(f"Iteraciones búsqueda lineal: {contador}")
            return i

    # Si no encuentra el valor, imprimir el número de iteraciones
    #print(f"Iteraciones búsqueda lineal: {contador}")
    return None

def buscar_binaria(lista: list, buscado: int) -> int:
    inicio = 0
    final = len(lista) - 1
    iteracion = 0

    while inicio <= final:
        medio = (inicio + final) // 2
        iteracion += 1
        if lista[medio] == buscado:
            print(f"Iteraciones busqueda binaria: {iteracion}")
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else: 
            final = medio - 1

    #print(f"Iteraciones: {iteracion}")  # Imprime las iteraciones si no encuentra el valor
    return None



