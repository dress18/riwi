# Solicita los tres lados de un triángulo. Comprueba si es válido y clasifícalo como equilátero, isósceles o escaleno.

print("Bienvenido")

lado1 = float(input("Ingrese el primer lado de su triangulo: "))
lado2 = float(input("Ingrese el segundo lado de su triangulo: "))
lado3 = float(input("Ingrese el tercer lado de su triangulo: "))

if lado1 == lado2 == lado3:
    print("Su triángulo es equilátero!")
elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3:
    print("Su triángulo es isósceles!")
else:
    print("Su triangulo es escaleno!")
