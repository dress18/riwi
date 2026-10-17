# Solicita un usuario y una contraseña. Compara los datos con valores definidos y permite el acceso si ambos coinciden.

print("bienvenido")

usuario = "riwi"
passw = "riwi123"

usuario_ = input("Ingrese su usuario: ")
passw_ = input("Ingrese su contraseña: ")

if usuario_ == usuario and passw_ == passw:
    print("Bienvenido... Su usuario y contraseña coinciden!")
else: 
    print("Intentelo de nuevo, su contraseña o usuario no coinciden.")