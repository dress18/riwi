Ejercicios de Bucles en Python
Objetivos
• Comprender la diferencia entre los distintos tipos de bucles en Python.
• Aplicar bucles en problemas reales utilizando contadores y acumuladores.
• Analizar cuál bucle es más eficiente para cada situación.
Ejercicios
1. Contar del 1 al 10 con diferentes bucles
En Python no existe el “hacer-mientras” de forma explícita, pero se puede simular con un
while True y un break.
# Usando while
i = 1
while i <= 10:
 print(i)
 i += 1
# Simulando do-while con while True
i = 1
while True:
 print(i)
 i += 1
 if i > 10:
 break
# Usando for
for i in range(1, 11):
 print(i)
2. Sumatoria de los primeros 10 números naturales
# Con for
suma = 0
for i in range(1, 11):
 suma += i
print("La suma es:", suma)
# Con while
suma = 0
i = 1
while i <= 10:
 suma += i
 i += 1
print("La suma con while es:", suma)
3. Cuenta regresiva de 10 a 1
i = 10
while i >= 1:
 print(i)
 i -= 1
print("¡Despegue!")
4. Cálculo de factorial
n = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, n+1):
 factorial *= i
print(f"El factorial de {n} es {factorial}")
5. Promedio de calificaciones
suma = 0
for i in range(5):
 nota = float(input(f"Ingrese la calificación {i+1}: "))
 suma += nota
promedio = suma / 5
print("El promedio es:", promedio)
if promedio >= 6:
 print("Aprobado")
else:
 print("Reprobado")
Reflexión y Discusión
1. ¿En qué situaciones es mejor usar un while y en cuáles un for?
2. ¿Qué ventajas tiene usar for cuando conocemos el número de repeticiones de
antemano?
3. ¿Cómo cambiarías los ejercicios si quisieras que el usuario decida cuándo parar en
lugar de usar un rango fijo?