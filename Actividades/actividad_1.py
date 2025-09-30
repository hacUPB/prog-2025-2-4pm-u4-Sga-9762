'''
# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500

# Conclusión: es posible asignar el valor de una variable a otras variables distintas, y cambiar el valor de otras variables sin afectar la variable 'original'.
'''
'''
velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))
'''

def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada