positivos = 0
negativos = 0

print("Ingrese varios valores (enteros), termine con cero:")

while True:
    numero = int(input())
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        break

print("Gráfico de números positivos:", "*" * positivos)
print("Gráfico de números negativos:", "*" * negativos)