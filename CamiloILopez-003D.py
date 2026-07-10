
def menuu():
    print("MENU PRINCIPAL" \
    "1. Cupos por tipo de plan." \
    "2. Busqueda de planes por rango de precio." \
    "3. Actualizar precio del plan." \
    "4. Agregar plan." \
    "5. Eliminar plan." \
    "6. Salir"
    )

def leer_opcion():
    while True:
        try:
            op = int("Ingrese una opcion: ")
            if 1 <= op <= 6:
                return
        except ValueError:
            print("Error: fuera de rango. ")

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_plan(plan):
    if plan ["MENSUAL", "TRIMESTRAL", "ANUAL"].lower():
        return True
    return False

def validar_texto(texto):
    if texto.strip() != "":
        return True
    return False

def nombre_plan(nombreplan):
    if nombreplan.strip() != "":
        return True
    return False

def duracion(duracionmes):
    if duracionmes > 0:
        return True
    return False


def horario_plan(horario):
    if horario.strip() != "":
        return True
    return False

def validar_cupos(cupos):
    if cupos >= 0:
        return True
    return False

def agregar_codigo(lista_codigo):
    codigo_plan = input("Ingrese su codigo: ")
    if not validar_texto(codigo_plan):
        return
    print("Error: no puede estar vacio o contener espacios. ")
    
    nombre_plan = input("Ingrese nombre del plan: ")
    if not validar_texto(nombre_plan):
        print("Error: no debe estar vacio ni contener espacios.")
        return
    
    tipo_plan = input("Ingrese tipo (mensual/trimestral/anual: )")
    if not validar_plan(tipo_plan):
        print("Error escriba uno de los seleccionados en pantalla.")
        return
    
    duracion_meses = int("Ingrese la duracion: ")
    if not duracion(duracion_meses):
        print("Error: ingrese numero entero.")
        return
    

    try:
        precio = int(input("Ingrese el precio: "))
    except ValueError:
        print("Error: debe ser un numero entero.")
    else:
        if not validar_precio(precio):
            return
        plan_mensual = int

    nuevocupo = {
        "codigo": codigo_plan,
        "nombre": nombre_plan,
        "duracion": duracion_meses,
        "precio": precio,
    }
    lista_codigo.append(nuevocupo)
    print(f"Registrado con exito {nuevocupo}")
