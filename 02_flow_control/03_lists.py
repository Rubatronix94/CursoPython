"""
03 - Listas
Secuencias mutables de elementos.
Pueden contener elementos de diferentes tipos.

Creación de listas
"""
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # Lista de cadenas
lista3 = [1.5, 2.5, 3.5] # Lista de flotantes
lista4 = [1, "dos", 3.0, True] # Lista con diferentes tipos
# lista_mezclada = ["manzanas", 1 ,  "peras", "plátanos"]

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]] # Lista de listas
matrix = [[1,2], [3,4], [5,6]] # Matriz 2x3


# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos (accede desde el último elemento)
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas T.2:01:52 
lista1 = [1, 2, 3, 4, 5]
print("\nSlicing de listas")
print(lista1[1:4])  # [2, 3, 4]
