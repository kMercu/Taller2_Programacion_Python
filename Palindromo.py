def es_palindromo(num):
    num_original = num
    invertido = 0

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num //= 10

    return num_original == invertido

num = int(input("Ingrese un número: "))

if es_palindromo(num):
    print(f"{num} es un palíndromo.")
else:
    print(f"{num} no es un palíndromo.")