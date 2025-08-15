"""
01 - Bucle while
Permite ejecutar un bloque de código mientras se cumpla una condición.
"""
# print("\nBucle while")
# contador = 0
# while contador < 5:
#     print("Contador:", contador)
#     contador += 1 # Importante para evitar un bucle infinito


# print("\nBucle con break")
# contador = 0
# while True:  # Bucle infinito
#     print("Contador:", contador)
#     contador += 1
#     if contador == 5:
#         break


### Continue: lo que hace es saltar esa iteraci0n en concreto y seguir con el bucle
contador = 0
while contador < 10:
    contador += 1

    if contador %2 == 0:
        continue

    print(contador)
    print("Aqui no llega si es par (Continue hace que siga con la siguiente iteración)") 



### Bucle While con else
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
else:
    print("Bucle while terminado")



print(input("Introduzca instrucciones: "))