# Pide n y muestra la suma de todos los números de 1 a n usando for, range y un acumulador

numero = int(input("Por favor ingrese un número: "))
acumulador = 0

for i in range(1, numero + 1):
    acumulador = acumulador + i
print(f"La suma es: {acumulador}")