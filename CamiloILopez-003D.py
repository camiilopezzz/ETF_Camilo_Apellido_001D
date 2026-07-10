
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

