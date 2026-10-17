# Solicita dos números y una operación (+, -, *, /). Muestra el resultado y evita la división entre cero.

print("Bienvenido")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación que desea hacer(+, -, *, /): ")

if operacion == "+":
    print(f"La suma de los número ses: {num1 + num2}")
elif operacion == "-":
    print(f"La resta de los números es: {num1 - num2}")
elif operacion == "*":
    print(f"La múltiplicación de los números es: {num1 * num2}")
elif operacion == "/":
    print(f"La división de los números es: {num1 / num2}")
else: 
    print("Ingrese una operación valida.")