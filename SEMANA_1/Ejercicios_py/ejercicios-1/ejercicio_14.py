"""
Crea un cajero con un saldo inicial de $500.000 y estas opciones:

Consultar saldo.
Retirar dinero.
Depositar dinero.
Salir.
"""

while True:
    print("---- Menú de opciones ----")
    print("1. Consultar saldo")
    print("2. Retirar saldo")
    print("3. Depositar dinero")
    print("4. salir")

    op = int(input("Ingrese su opción: "))
    saldo = 500000

    if op == 1:
        print(f"Su saldo actual es: ${saldo}")
    elif op == 2:
        op = int(input("¿Cuánto desea retirar?: $"))

        saldo = saldo - op
        if saldo < 0:
            print("Intentelo de nuevo su saldo es insuficiente\n")
            continue
        print(f"Retiro exitoso! Su saldo es: ${saldo}")
    elif op == 3:
        op = int(input("¿Cuánto desea depositar?: $"))
        
        saldo = saldo + op
        if saldo < 0:
            print("Intentelo de nuevo, no puede depositar saldo negativo\n")
            continue
        print(f"Deposito exitoso! Su saldo es: ${saldo}\n")
    elif op == 4:
        print("Saliendo del cajero...\n")
        break
    else:
        print("Por favor ingrese una opción valida!\n")
