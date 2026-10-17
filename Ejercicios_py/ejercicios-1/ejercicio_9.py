"""
Solicita el precio de una compra:

$200.000 o más: 20 % de descuento.
$100.000 o más: 10 % de descuento.
Menos de $100.000: sin descuento.
Muestra el total a pagar.
"""

print("Bienvenido")

compra = float(input("Ingrese el precio de su compra en pesos COP: "))
desc = 0

if compra >= 200000:
    desc = 0.20
    print("Usted tiene un descuento del 20% por su compra")
    print(f"Su valor total a pagar es: {compra - (compra * desc)}")
elif compra >= 100000:
    desc = 0.10
    print("Usted tiene un descuento del 10% por su compra")
    print(f"Su valor total a pagar es: {compra - (compra * desc)}")
else: 
    print(f"Usted no recibe descuento su valor total a pagar es: {compra}")