# Pide un texto y cuenta cuántas vocales tiene, sin importar si están en mayúscula o minúscula.

palabra = input("Ingresa una palabra: ")
i = 0

for p in palabra:
    if p.lower() in "aeiou":
        i += 1

print("EL número de vocales que tiene es: ", i)