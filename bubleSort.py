from os import system
system("cls")

def validar_lista(lista: list) -> list:
    if type(lista) != list:
        return None
    else: 
        return lista
    
def blue_short(lista: list) -> list:
    n  = len(lista)
    for i in  range (n):
        print(f"Iteración {i}")
        intercambio = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                intercambio = True
                menor = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = menor
                print(lista)
        
        if intercambio == False:
            print(f"Dejo de correr en la iteracción {i}")
            break
        
    return lista

def blue_short_mayor(lista: list) -> list:
    n  = len(lista)
    for i in  range (n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1] :
                mayor = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = mayor
    return lista

lista = [25, 50, 78, 2, 12, 1]
valida = validar_lista(lista)
if valida != None:
    print(f"Lista de menor a mayor: {blue_short(lista)}")
    print(f"Lista de mayor a menor: {blue_short_mayor(lista)}")
else:
    print("La lista no es valida")


    
