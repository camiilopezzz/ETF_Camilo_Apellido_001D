plan = ["MENSUAL", "mensual", "TRIMESTRAL", "trimestral", "ANUAL", "anual",]

planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}
def menuu():
    print(" MENU PRINCIPAL   "
    "   1. Cupos por tipo de plan. "
    "   2. Busqueda de planes por rango de precio. "
    "   3. Actualizar precio del plan. "
    "   4. Agregar plan. "
    "   5. Eliminar plan. "
    "   6. Salir "
    )

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if  1 <= op <= 6:
                return op
        except ValueError:
            print("Error")
def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_plan(plan):
    if plan.lower():
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

def preciomaximomin(maxmin):
    if maxmin >= 0:
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
    
    duracion_meses = int(input("Ingrese la duracion: "))
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

    planes = {
        "codigo": codigo_plan,
        "nombre": nombre_plan,
        "duracion": duracion_meses,
        "precio": precio,
    }
    lista_codigo.append(planes)
    print(f"Registrado con exito {planes}")

def buscar_codigo(lista_codigo, busqueda_codigo):
    op = int(input("Ingrese codigo a buscar: "))
    for i in range(len(lista_codigo, op)):
        if lista_codigo[i]["codigo"].lower() == busqueda_codigo.lower():
            return i
    return -1


def eliminar_codigo(lista_codigo):
    nom = int(input("Ingrese codigo a eliminar: "))
    indice = buscar_codigo(lista_codigo, nom)
    if indice == -1:
        print ("Error codigo no encontrado. ")
        return -1
    else:
        lista_codigo.pop(indice)
        print(f"Codigo encontrado en la posicion {indice}")

def main():
    lista_codigo = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
        }
    menuu()
    opcio = leer_opcion()
    while True:
        match opcio:
            case 3: buscar_codigo(lista_codigo)
            case 4: agregar_codigo(lista_codigo)
            case 5: eliminar_codigo(lista_codigo)
            case 6:
                print("Programa Finalizado.")
                break

main()

