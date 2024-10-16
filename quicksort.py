from os import system
system("cls")
def ordenar_rapido(lista: list) -> list:

    '''
    Ordena los elementos mediante "divide y vencerás" usando un pivote.
    Recibe una lista.
    Devuelve una lista.
    '''

    if type(lista) != list:
        print("El parámetro de la función debe ser una lista")
        return None
    
    menores = []
    iguales = []
    mayores = []

    if len(lista) > 1:

        pivote = lista[0]

        for i in range(len(lista)):
            
            lista_nueva = [lista[i]]
            
            if lista[i] < pivote:            
                menores += lista_nueva
            elif lista[i] == pivote:
                iguales += lista_nueva
            else:
                mayores += lista_nueva

        return ordenar_rapido(menores) + iguales + ordenar_rapido(mayores)
    
    else:
        return lista
    
lista = [25, 50, 78, 2, 12, 1]
ordena = ordenar_rapido(lista)
if ordena != None:
    print(f"La lista ordenada de menor a mayor es: {ordena}")