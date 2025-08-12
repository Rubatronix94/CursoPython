""""
numero = 5
if numero: # True
    print("El número no es cero")

numero = 0
if numero: # False
    print("En este fragmento no entra")

#-------------------------

nombre = "Python"
if nombre: # True
    print("El nombre no está vacío")

nombre = ""
if nombre: # False
    print("En este fragmento no entra")

#-------------------------

numero = 5 # asignacion
numero == 3 # comparacion
es_el_tres = numero == 3 # puede usarse como variable booleana

if es_el_tres: # False
    print("El número es 3")

"""

print("\nLa condición ternaria:")
# es una forma de simplificar un if-else
# [código si cumple la condición] if [condición] else [código si no cumple]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

if n1 > n2:
    print(f"El número mayor es: {n1}")
elif n1 < n2:
    print(f"El número mayor es: {n2}")
else:
    print("Los números son iguales.")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = n1 + n2
elif operacion == "-":
    resultado = n1 - n2
elif operacion == "*":
    resultado = n1 * n2
elif operacion == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Error: División entre cero no permitida."
else:
    resultado = "Operación no válida."

print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# año = int(input("Introduce un año: "))
# if (año % 4 == 0 and año % 100 != 0 and año % 400 != 0):
#     print(f"{año} es un año bisiesto.")

año = int(input("Introduce un año: "))
if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
edad = int(input("Introduce tu edad: "))
if edad < 0 and edad > 2:
    print("Bebe.")
elif edad >= 3 and edad <= 12:
    print("Niño.")
elif edad >= 13 and edad <= 17:
    print("Adolescente.")
elif edad >= 18 and edad <= 64:
    print("Adulto.")
else:
    print("Adulto mayor.")

# Ejercicio 5: Par o impar
num = int(input("Introduce un número: "))
if num % 2 == 0:
    print(f"{num} es un número par.")
elif num % 2 != 0:
    print(f"{num} es un número par.")
