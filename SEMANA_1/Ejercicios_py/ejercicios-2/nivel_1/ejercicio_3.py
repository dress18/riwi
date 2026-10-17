#Pedir un númeroy hacerle la tabla de multiplicar
numero = int(input("Por favor ingrese un número: "))

for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")