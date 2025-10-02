# DICCIONARIOS
MANTO = {} #REGISTRO: {tipo, antiguedad, ciclos de vuelo, estado, última fecha MANTO, prioridad MANTO}

opcion = int(input("¿Desea agregar una aeronave al calendario de mantenimiento?\n1. SI\n2. NO\nSELECCIÓN: "))
opcion2 = int(input("¿Desea modificar una aeronave en el calendario?\n1. SI\n2. NO\nSELECCIÓN: "))
space = "=="*50
match opcion:
    case 1:
        print(space)
        reg = str(input("Ingrese el registro de la aeronave: "))
        type = str(input("Ingrese el tipo de aeronave (A320, 737, 787...): "))
        age = int(input("Ingrese la antiguedad de la aeronave(en años): "))
        cycle = float(input("Ingrese la cantidad de ciclos de la aeronave: "))
        state = int(input("Ingrese el estado de la aeronave\n1. EN SERVICIO\n2. A.O.G\n3. PRESERVADO\nSELECCION: "))
        lastchk = str(input("Ingrese la fecha del último chequeo de mantenimiento: "))
        priority = str(input("Ingrese la prioridad del mantenimiento\n1. ***ALTO***\n2. **MEDIO**\n3. *BAJO*\nSELECCION: "))
        biblio = {f"Modelo: {type}", age, cycle, state, lastchk, priority}
        MANTO[f"{reg}"] = biblio
        print(MANTO)

    case 2:
        pass
    case _:
        print("Opción inválida")
