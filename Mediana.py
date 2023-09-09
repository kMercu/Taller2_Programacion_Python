numeros = []

print("Ingrese números ordenados (ingrese '.' para terminar):")

while True:
    entrada = input()
    if entrada == ".":
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida. Ingrese un número o '.' para finalizar.")

n = len(numeros)

if n % 2 == 1:
    mediana = numeros[n // 2]
    print(f"La mediana es: {mediana}")
else:
    num1 = numeros[n // 2 - 1]
    num2 = numeros[n // 2]
    mediana = (num1 + num2) / 2
    print(f"La mediana es: {mediana}")