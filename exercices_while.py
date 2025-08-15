# Ejercicio 1: Cuenta atrás
print("\nEjercicio 1:")
contador = 10
while contador > 0:
    print("Cuenta atrás:", contador)
    contador -= 1
print("¡Despegue!")

# Ejercicio 2: Suma de números pares (while)
print("\nEjercicio 2:")
pares = []
contador = 1
while contador <= 20:
    if contador % 2 == 0:
        pares.append(contador)
    contador += 1
print("Números pares:", pares)
print("Suma total:", sum(pares))

# Ejercicio 3: Factorial de un número
print("\nEjercicio 3:")
try:
    input_num = int(input("Introduce un número entero positivo para calcular su factorial: "))
    factorial = 1
    contador = 1
    while contador <= input_num:
        factorial *= contador
        contador += 1
    print(f"El factorial de {input_num} es {factorial}")
except ValueError:
    print("Error: Debes introducir un número entero válido.")

# Ejercicio 4: Validación de contraseña
print("\nEjercicio 4:")
try:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    while len(password) < 8:
        print("Contraseña inválida. Inténtalo de nuevo.")
        password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    print("Contraseña válida.")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Ejercicio 5: Tabla de multiplicar
print("\nEjercicio 5:")
try:
    num = int(input("Introduce un número para ver su tabla de multiplicar: "))
    multiplicador = 1
    while multiplicador <= 10:
        print(f"{num} x {multiplicador} = {num * multiplicador}")
        multiplicador += 1
except ValueError:
    print("Error: Debes introducir un número válido.")

# Ejercicio 6: Números primos hasta N
print("\nEjercicio 6:")
try:
    N = int(input("Introduce un número entero positivo: "))
    numero = 2
    while numero <= N:
        es_primo = True
        divisor = 2
        while divisor <= numero // 2:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor += 1
        if es_primo:
            print(numero, end=" ")
        numero += 1
    print()
except ValueError:
    print("Error: Debes introducir un número entero válido.")

# Pausa final para que no se cierre la consola
input("\nPulsa Enter para salir...")
