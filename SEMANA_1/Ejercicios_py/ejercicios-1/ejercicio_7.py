# Solicita la edad de una persona e indica si puede ingresar a un evento para mayores de 18 años. Valida que la edad no sea negativa.

print("Bienvenido")

num1 = int(input("Ingrese su edad: "))

if num1 >= 18:
    print("Usted puede ingresar al remate de hallowen")
elif num1 < 0:
    print("Su edad es invalida, por favor intentelo de nuevo.")
else: 
    print("Usted es menor de edad y por ende no puede entrar a la fiesta")