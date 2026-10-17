# Solicita dos números y una operación (+, -, *, /). Muestra el resultado y evita la división entre cero.

print("Bienvenido")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("---- Menú de opciones ----")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
operacion = int(input("Ingrese el número de la operación que desea hacer: "))

if operacion == 1:
    print(f"La suma de los números es: {num1 + num2}")
elif operacion == 2:
    print(f"La resta de los números es: {num1 - num2}")
elif operacion == 3:
    print(f"La múltiplicación de los números es: {num1 * num2}")
elif operacion == 4:
    print(f"La división de los números es: {num1 / num2}")
else: 
    print("Ingrese una operación valida.")