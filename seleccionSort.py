from os import system
system("cls")

lista = [25, 50, 78, 2, 12, 1]

def ordenar_x_seleccion(lista: list) -> list:

    '''
    Ubica iterativamente el menor valor de la lista en el índice menor.
    Recibe una lista.
    Devuelve una lista.
    '''

    for i in range(len(lista) - 1):
        indice_menor = i #posición en la que queremos ubicar el elemento menor

        print(f"El índice es {i}")

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j #posición del elemento con menor valor 

        if indice_menor != i:
            menor = lista[indice_menor]
            print(f"El elemento menor es {menor}")
            lista[indice_menor] = lista[i]
            lista[i] = menor
            print(lista)
    
    return lista

seleccion = ordenar_x_seleccion(lista)
print(seleccion)