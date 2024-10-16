from os import system
system("cls")

lista_nueva_4 = [0] * 5
print(lista_nueva_4)

# Podemos cargar listas secuencialmente
for i in range(len(lista_nueva_4)):
    lista_nueva_4[i] = input(f"Ingrese un nombre para la posición {i}: ")

print(lista_nueva_4)