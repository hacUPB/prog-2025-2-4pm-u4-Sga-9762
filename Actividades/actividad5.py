# DICCIONARIOS
MANTO = {} #REGISTRO: {tipo, antiguedad, ciclos de vuelo, estado, última fecha MANTO, prioridad MANTO}

opcion = int(input("¿Desea agregar una aeronave al calendario de mantenimiento?\n1. SI\n2. NO\nSELECCIÓN: "))
opcion2 = int(input("¿Desea modificar una aeronave en el calendario?\n1. SI\n2. NO\nSELECCIÓN: "))
space = "=="*50

estados = ("EN SERVICIO", "A.O.G.", "PRESERVADO")
pr = ("ALTO", "MEDIO", "BAJO")
match opcion:
    case 1:
        print(space)
        reg = str(input("Ingrese el registro de la aeronave: "))
        type = str(input("Ingrese el tipo de aeronave (A320, 737, 787...): "))
        age = int(input("Ingrese la antiguedad de la aeronave(en años): "))
        cycle = float(input("Ingrese la cantidad de ciclos de la aeronave: "))
        state = int(input(f"Ingrese el estado de la aeronave\n1. {estados[0]}\n2. {estados[1]}\n3. {estados[2]}\nSELECCION: "))
        lastchk = str(input("Ingrese la fecha del último chequeo de mantenimiento: "))
        priority = int(input("Ingrese la prioridad del mantenimiento\n1. ***ALTO***\n2. **MEDIO**\n3. *BAJO*\nSELECCION: "))
        estado = None

        biblio = {type, age, cycle, estados[state-1], lastchk, pr[priority-1]}
        MANTO[f"{reg}"] = biblio
        print(MANTO)

    case 2:
        print(MANTO)
    case _:
        print("Opción inválida")
