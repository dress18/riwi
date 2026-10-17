# Solicita una nota de 0 a 100 e indica si el estudiante está aprobado (70 o más) o reprobado. Valida la nota.

print("Bienvenido")

num1 = int(input("Ingrese su nota de 0 a 100: "))

if num1 >= 70:
    print("Usted está aprobado!")
elif num1 < 0:
    print("Su nota es invalida, por favor intentelo de nuevo.")
else: 
    print("Usted está reprobado!")
