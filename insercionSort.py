from os import system
system("cls")

lista = [25, 50, 78, 2, 12, 1]

def insercion_sort(lista: list) -> list:
    for i in range(1, len(lista)):
        print(f"Iteración {i}")
        auxiliar = lista[i]
        j = i - 1
        while j >= 0 and auxiliar < lista[j] :
                print(f"Intercambio {lista[j]} con {lista[j+1]}")
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = auxiliar
    return lista

insercion = insercion_sort(lista)
print(insercion)