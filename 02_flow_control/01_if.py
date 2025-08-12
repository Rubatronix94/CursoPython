# Sentencias condicionales (if, elif y else)

edad = 20

if edad <= 17:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un anciano")

"""
En vez de llaves {}, Python usa 2 puntos :
 e indentación
 """    

age=16
if age <= 18:
    print("Eres mayor de edad")
    print("Puedes conducir!!")
else:
    print("Eres menor de edad")

""" Else: no es recomendable bifucrcar el código

Condicionales con elif """
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5:
    print("Notable")
else:
    print("No está aprobado")

# Ejecuta codigo en orden, al primero que entra
# es el que imprime. Orden descendente

print("\n Condicionales multiples (AND)")
edad = 20
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")