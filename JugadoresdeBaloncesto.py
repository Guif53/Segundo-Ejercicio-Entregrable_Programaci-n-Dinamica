import random
from prettytable import PrettyTable

# Generar una lista de entre 6 y 10 jugadores con habilidades aleatorias
def generar_jugadores():
    num_jugadores = random.randint(6, 10)
    jugadores = []
    for i in range(1, num_jugadores + 1):
        jugador = {
            "nombre": f"Jugador {i}",
            "tiros": random.randint(10, 20),
            "defensa": random.randint(10, 20),
            "condicion_fisica": random.randint(10, 20),
            "dribling": random.randint(10, 20)
        }
        jugadores.append(jugador)
    return jugadores

# Encontrar el área más débil de un jugador
def area_menor_habilidad(jugador):
    habilidades = {"tiros": "Tiros de Media Distancia", "defensa": "Defensa en Equipo", 
                   "condicion_fisica": "Condición Física", "dribling": "Dribling"}
    menor_habilidad = min(habilidades.keys(), key=lambda x: jugador[x])
    return menor_habilidad, habilidades[menor_habilidad]

# Mejorar la habilidad del jugador en el área entrenada
def mejorar_habilidad(jugador, area):
    jugador[area] += 20

# Planificar los entrenamientos
def planificar_entrenamiento(jugadores, entrenamientos, tiempo_total):
    plan_entrenamiento = []
    tiempo_por_jugador = tiempo_total // len(jugadores)  # Tiempo por jugador

    # Asignar entrenamientos según el área más débil de cada jugador
    for jugador in jugadores:
        area, entrenamiento = area_menor_habilidad(jugador)
        plan_entrenamiento.append({
            "jugador": jugador["nombre"],
            "entrenamiento": entrenamiento,
            "duracion": tiempo_por_jugador
        })
        mejorar_habilidad(jugador, area)

    return plan_entrenamiento

# Generar una tabla inicial de habilidades
def generar_tabla_habilidades(jugadores):
    tabla = PrettyTable()
    tabla.field_names = ["Nombre", "Tiros", "Defensa", "Condición Física", "Dribling"]
    for jugador in jugadores:
        tabla.add_row([jugador["nombre"], jugador["tiros"], jugador["defensa"], 
                       jugador["condicion_fisica"], jugador["dribling"]])
    return tabla

# Datos iniciales
jugadores = generar_jugadores()

# Generar la tabla inicial de habilidades
tabla_inicial = generar_tabla_habilidades(jugadores)

# Planificar el entrenamiento
entrenamientos = ["Tiros de Media Distancia", "Defensa en Equipo", "Condición Física", "Dribling"]
tiempo_total = 180  # Tiempo total disponible en minutos
plan_entrenamiento = planificar_entrenamiento(jugadores, entrenamientos, tiempo_total)

# Generar la tabla final de habilidades
tabla_final = generar_tabla_habilidades(jugadores)

# Imprimir la tabla inicial de habilidades
print("Tabla inicial de habilidades:")
print(tabla_inicial)

# Imprimir el plan de entrenamiento
print("\nPlan de Entrenamiento:")
for sesion in plan_entrenamiento:
    print(f"Jugador: {sesion['jugador']} | Entrenamiento: {sesion['entrenamiento']} | Duración: {sesion['duracion']} minutos")

# Imprimir la tabla final de habilidades
print("\nTabla final de habilidades:")
print(tabla_final)

# Análisis del tiempo utilizado
tiempo_usado = sum(sesion["duracion"] for sesion in plan_entrenamiento)
print(f"\nTiempo total disponible: {tiempo_total} minutos")
print(f"Tiempo utilizado: {tiempo_usado} minutos")
print(f"Tiempo restante: {tiempo_total - tiempo_usado} minutos")
