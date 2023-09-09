import random

numero_secreto = random.randrange(101)

intentos = 0

print("Adivina el número entre 0 y 100.")

while True:
    intento = int(input("Intento {}:".format(intentos + 1)))
    intentos += 1

    if intento < numero_secreto:
        print("Es mayor que", intento)
        print()
    elif intento > numero_secreto:
        print("Es menor que", intento)
        print()
    else:
        print("Correcto. Adivinaste en {} intentos.".format(intentos))
        print()
        break