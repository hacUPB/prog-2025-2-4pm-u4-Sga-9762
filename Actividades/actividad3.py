'''
# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)


# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado con *
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")
'''
'''
lista_tuplas = [(0,0), (3,5), (8.3)]
lista_tuplas.append((7,5))
print(lista_tuplas)
lista_tuplas[0] = (4, 3) 
print(lista_tuplas) # Se puede reemplazar (0,0), puesto que hace parte de una lista. Sin embargo, los contenidos **dentro** de (0,0) no se pueden cambiar
# lista_tuplas[0][0] = 1 -> no se puede hacer, puesto que las tuplas son inmutables -> [x][y] significa: índice 'x', elemento 'y' del índice 'x'

tupla_dlistas = ([3,2,0], [2,7,4])
tupla_dlistas[1][1] = 8 # se puede cambiar el elemento 1 de la primera **lista**, puesto que no se está alterando la tupla, solo la lista.
print(tupla_dlistas)
'''
'''
# EJERCICIO DE PRÁCTICA
fleet = [
    ("N284AV", "100 Years Livery", "11 years", "Airbus A320"), # reg, livery, age, type/model
    ("N567AV", "TACA Heritage Livery", "12 years", "Airbus A320"),
    ("N477AV", "Star Alliance Livery", "13 years", "Airbus A320"),
    ("N821AV", "LACSA Heritage Livery", "14 years", "Airbus A320"),
    ("N776AV", "Aerogal Heritage Livery", "6 years", "Airbus A320neo"),
    ("N799AV", "Biodiversity Livery", "8 years", "Boeing 787-8"),
]

fleet.append(("N398AV", "Aviateca Heritage Livery", "14 years", "Airbus A320"))
space = "=="*50
def print_fleet():
    print(space)
    print("**CATÁLOGO DE FLOTA**")
    for i in fleet:
        reg = i[0]
        liv = i[1]
        age = i[2]
        type = i[3]

        print(f"**Aeronave encontrada:**\n Registro: {reg}\n Livery: {liv}\n Antiguedad: {age}\n Tipo: {type}\n {space}")


flag = True

while True:
    opcion = int(input("¿Desea agregar una aeronave al inventario?\n1. SI\n2. NO\nSELECCIÓN: "))
    match opcion:
        case 1:
            matr = str(input("Ingrese la matrícula del avión: "))
            pintura = int(input("¿Tipo de pintura?\n1. 2013 Livery\n2. 2023 Livery\n3. Heritage Livery/Special Livery\n. SELECCIÓN: "))
            livery = None
            if pintura == 1:
                livery = "2013 Livery"
            elif pintura == 2:
                livery = "2013 Livery"
            elif pintura == 3:
                livery = str(input("Ingrese la denominación del livery: "))
            antiguo = str(input("Ingrese la antigüedad del avión: "))
            avion = str(input("Ingrese el modelo del avión: "))
            fleet.append((matr, livery, antiguo, avion))
            print(space)
            opt = int(input("¿Desea visualizar la lista de la flota?\n1. SI\n2. NO\nSELECCIONE: "))
            if opt == 1:
                print_fleet()
        case 2:
            print(space, "SISTEMA APAGADO")
            break
        case _:
            print("Comando inválido")
    pass
'''
