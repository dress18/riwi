#Con notas = [4.5, 2.8, 3.9, 3.0, 2.2] calcula el promedio y cuántos aprobaron (nota ≥ 3.0).

notas = [4.5, 2.8, 3.9, 3.0, 2.2]
i = 0
a = 0
aprobados = 0
promedio = 0

for nota in notas:
    a = a + nota
    i += 1
    
    if nota >= 3.0:
        aprobados += 1

promedio = a / i


print("El promedio de las notas es: ", promedio)
print("Los estudinates aprobados(>= 3.0): ", aprobados)