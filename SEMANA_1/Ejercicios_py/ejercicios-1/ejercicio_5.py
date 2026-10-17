# Solicita dos números e indica cuál es mayor o si son iguales.

print("Bienvenido")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El primer número ingresado ({num1}) es mayor al segundo número ingresado ({num2})")
else:
    print(f"El segundo número ingresado ({num2}) es mayor al primer número ingresado ({num1})")