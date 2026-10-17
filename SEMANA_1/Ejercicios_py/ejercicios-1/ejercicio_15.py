"""
Solicita el nombre del cliente, el producto, su precio y la cantidad. Calcula el subtotal y aplica estos descuentos:

$500.000 o más: 15 %.
$200.000 o más: 10 %.
Menos de $200.000: sin descuento.
Muestra una factura con el subtotal, el descuento y el total a pagar.

"""

nombre = input("Ingrese su nombre: ")
produc = input("Ingrese el nombre de su producto: ")
precio = int(input("Ingresa el precio de su producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

desc = 0
subtotal = 0
total = 0

subtotal = cantidad * precio

if subtotal >= 500000:
    desc = subtotal * 0.15
    total = subtotal - desc
elif subtotal >= 200000:
    desc = subtotal - 0.10
    total = subtotal - desc
else:
    total = subtotal

print(f"\n---- FACTURA ----")
print(f"- Factura a nombre de: {nombre}")
print(f"- Producto: {produc}")
print(f"- Precio producto: ${precio}")
print(f"- Cantidad: {cantidad}")
print(f"- SUBTOTAL: ${subtotal}")
print(f"- Descuento: {desc}")
print(f"- Cantidad: {cantidad}")
print(f"- TOTAL: {total}")








