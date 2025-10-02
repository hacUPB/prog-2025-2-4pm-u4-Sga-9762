'''
# Indexación (comienza en 0)
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa)

# Slicing (rebanado)
print(componentes[1:3])  # ["fuselaje", "motores"]
print(componentes[:2])   # ["alas", "fuselaje"]
print(componentes[2:])   # ["motores", "tren de aterrizaje"]
'''
'''
import random
lista = []
lista.append(50)
num = int(input("Ingrese un número: "))
lista.append(num)
print(lista)
for i in range(10):
    aleat = random.randint(0, 100)
    #print(id(aleat))
    lista.append(aleat)
print(lista)
'''
'''
# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

sum = 0
for spd in velocidad: #Sumar cada elemento en la tabla 'velocidad'.
    sum += spd

spd_avg = sum/len(velocidad)
print(f"La velocidad promedio en vuelo fue de {spd_avg}km/h")

for elemento in velocidad: #Imprimir las velocidades que están por encima del promedio
    if elemento > spd_avg:
        print(f"Se ha encontrado una velocidad por encima del promedio: {elemento}km/h")
'''
'''
# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [2, 2, 0, -2, 2, -6]

# Cálculo del centro de masa en eje X sin list comprehensions
masa_total = 0
momento_total = 0

for i in range(len(masas)):
    masa_total += masas[i]
    momento_total += masas[i] * posiciones_x[i]

centro_masa_x = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m")

# Imprimir cuánto pesa cada componente del avión:

for c, m in zip(componentes, masas):
    print(f"Componente: {c} | Peso total: {m}kg")
'''

# Registro de temperaturas del motor durante un vuelo
temperaturas_motor = [120, 350, 380, 375, 390, 400, 405, 390, 385, 370]

# Añadir nueva lectura
temperaturas_motor.append(360)

# Encontrar temperatura máxima
temp_max = max(temperaturas_motor)
print(f"Temperatura máxima: {temp_max}°C")

# Encontrar posición de la temperatura máxima
pos_max = temperaturas_motor.index(temp_max)
print(f"Temperatura máxima alcanzada en la lectura #{pos_max+1}")

# Ordenar para análisis
temperaturas_ordenadas = sorted(temperaturas_motor)  # No modifica la original
print(f"Temperaturas ordenadas: {temperaturas_ordenadas}")

# Modificar la lista original
temperaturas_motor.sort(reverse=True)  # Orden descendente
print(f"Temperaturas (mayor a menor): {temperaturas_motor}")