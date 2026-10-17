# Solicita dos números, calcula su suma y resta. Indica si la suma es mayor que 10.

print("Bienvenido")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2

print(f"La suma de los dos números es: {suma}")
print(f"La resta de los dos números es: {resta}")

if suma > 10:
    print("La suma de los números es mayor a 10.")
