"""
Solicita una temperatura y clasifícala:

Menos de 10 °C: frío.
De 10 a menos de 25 °C: templado.
De 25 a menos de 35 °C: caluroso.
35 °C o más: muy caluroso.
"""

print("Bienvenido")

clima = int(input("Ingrese la temperatura actual: "))

if clima < 10:
    print("El clima está frio!")
elif clima >= 10 and clima <= 25:
    print("El clima está templado!")
elif clima > 25 and clima < 35:
    print("El clima está caluroso!")
else:
    print("El clima actual es muy caluroso!")