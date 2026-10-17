# Recorre del 1 al 20, salta los múltiplos de 5 con continue y cuenta cuántos pares e impares quedan.
pares = 0
impares = 0

for n in range(1, 21):
    if n % 5 == 0:
        continue

    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Pares: ", pares)
print("Impares: ", impares)