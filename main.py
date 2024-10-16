
import pruebas.ejercicio1 as fn
#from pruebas import *
lista = [95, 3, 55, 4, 6, 9, 13, 12, 10, 99,
            33, 22, 53, 44, 67, 69, 34, 19, 86, 100]

numero = 1
binario = 36

valida = fn.validar_lista(lista)
buscado = fn.buscar_lineal(lista, numero)


"""if valida is not None:
    ordena = fn.ordenar_lista(lista)
    descendente = fn. ordenar_descendente(lista)
    print(f"Lista ordenada ascendente: {ordena}")
    print(f"Lista ordenada descendente: {descendente}")
else:
    print("La lista no es valida")"""

if buscado is not None:
    print(f"El numero {numero} se encuentra en la posicion {buscado}")
else:
    print(f"El numero {numero} no se encuentra en la lista")

ordenar = fn.ordenar_lista(lista)
bin = fn.buscar_binaria(ordenar, binario)
if bin is not None:
    print(f"El numero {binario} se encuentra en la posicion {bin}")
else:
    print(f"El numero {binario} no se encuentra en la lista")