total_minutos = 0

print("Ingrese los tiempos de viaje en minutos (0 para finalizar):")

while True:
    tiempo_tramo = int(input("Tiempo del tramo (minutos): "))
    
    if tiempo_tramo == 0:
        break
    
    total_minutos += tiempo_tramo

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"El tiempo total de viaje es: {horas} horas {minutos} minutos")