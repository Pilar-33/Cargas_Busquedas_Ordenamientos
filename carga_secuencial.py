from os import system
system("cls")

lista = [0] * 5


def obtener_tipo_dato(elemento: any) -> any:
    entero = True
    decimal = False
    punto_decimal = False

    if elemento[0] == '-':
        inicio = 1
    else:
        inicio = 0
    
    for i in range(inicio, len(elemento)):
        if elemento[i] == '.' and not punto_decimal:
            entero = False
            decimal = True
            punto_decimal = True
        elif elemento[i] < '0' or elemento[i] > '9':
            entero = False
            decimal = False
            break

    
    if entero == True:
        return int(elemento)
    elif decimal == True:
        return float(elemento)
    return elemento



def cargar_secuencial(lista: list) -> list:
    for i in range(len(lista)):
        entrada = input(f"Ingrese dato para la posición {i}: ")
        lista[i] = obtener_tipo_dato(entrada)
        
    return lista

secuencial = cargar_secuencial(lista)
print(secuencial)