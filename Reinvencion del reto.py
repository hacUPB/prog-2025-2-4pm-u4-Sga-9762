# 1) Diccionario para la configuración
configuracion = {
        "initCG": 22.5,
        "uprLMT": 25,
        "lwrLMT": 20
    }
# 2) Lista de tuplas para las opciones del menú

# 4) Diccionario para centralizar los mensajes (adaptado para f-strings)
mensajes = {
        "input_flt": "Ingrese la duración del vuelo (horas): ",
        "iteracion": "Iteración actual: ",
        "menu_opciones": "Seleccione la sección de tanques de combustible a consumir:\n 1. ALAS\n 2. FUSELAJE CENTRAL\n",
        "menu_info": "**¡IMPORTANTE! RANGO DE CG SEGURO: entre ",
        "alerta_estabilidad": "¡ALERTA! ESTABILIDAD CRITICA. MODIFIQUE EL CENTRO DE GRAVEDAD INMEDIATAMENTE",
        "aterrizaje_seguro": "¡Aterrizaje seguro! CG actual: ",
        "aterrizaje_peligroso": "¡ATERRIZAJE PELIGROSO! CG actual: ",
        "historial_cg": "Historial de CG durante el vuelo: ",
        "error_vuelo": "El tiempo de vuelo ingresado no es válido."
    }

opciones_cg = [
        ("ALAS", -0.3),
        ("FUSELAJE CENTRAL", 0.5)
    ]
def fuelsim():

    
    flt = int(input(mensajes["input_flt"]))
    currentCG = configuracion["initCG"]
    
    # 3) Almacenar el historial de CG en una lista
    cg_history = [currentCG]
    
    i = 1
    
    while i <= flt and 0 < flt < 20:
        print(f'{mensajes["iteracion"]}{i}')
        
        menu_completo = (
            f'{mensajes["menu_opciones"]}'
            f'{mensajes["menu_info"]}{configuracion["lwrLMT"]}% y {configuracion["uprLMT"]}% \n'
            f' CG actual: {currentCG:0.2f}\n SU SELECCION: '
        )
        opcion_tanque = int(input(menu_completo))
        
        if opcion_tanque == 1:
            currentCG += opciones_cg[0][1]
        elif opcion_tanque == 2:
            currentCG += opciones_cg[1][1]
        
        cg_history.append(currentCG)
        
        if configuracion["uprLMT"] < currentCG < configuracion["lwrLMT"]:
            print(mensajes["alerta_estabilidad"])
        i += 1

    if configuracion["lwrLMT"] < currentCG < configuracion["uprLMT"] and 0 < flt < 20:
       print(f'{mensajes["aterrizaje_seguro"]}{currentCG}')
       for a in cg_history:
        print(f'{mensajes["historial_cg"]}{a:0.2f}')
        #print(f'{mensajes["historial_cg"]}{cg_history}')
    elif currentCG < configuracion["lwrLMT"] or currentCG > configuracion["uprLMT"]:
       print(f'{mensajes["aterrizaje_peligroso"]}{currentCG}')
       for a in cg_history:
        print(f'{mensajes["historial_cg"]}{a:0.2f}') 
        #print(f'{mensajes["historial_cg"]}{cg_history}')
    
    if flt >= 20 or flt <= 0:
       print(mensajes["error_vuelo"])
           
    return currentCG
bar = "="*25
def diccionarios(obj, name):
   print(f"Objetos encontrados en {name}:")
   for i, j in obj.items():
      print(i, ":", j)
   print(bar*2)

def listas(obj, name):
    print(f"Objetos encontrados en {name}:")
    for i, j in obj:
        print(i, ":", j)
    print(bar*2)


opcion = int(input("¡Bienvenido al programa! Seleccione una opción a continuación:\n1. EJECUTAR CÁLCULOS DE CENTRO DE GRAVEDAD\n" \
    "2. IMPRIMIR DICCIONARIOS\n3. IMPRIMIR LISTA\n SELECCIÓN: "))
match opcion:
        case 1:
          print("Ejecutando programa...")
          fuelsim()
        case 2:
          print(f"{bar}IMPRIMIENDO{bar}")
          diccionarios(mensajes, "mensajes")
          diccionarios(configuracion, "configuracion")
        case 3:
            print(f"{bar}IMPRIMIENDO{bar}")
            listas(opciones_cg, "opciones_cg")
        case 4:
            print("..Saliendo..")
            print(bar)
        case _:
          print("Opción inválida")


#fuelsim()

