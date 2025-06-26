patologías = [
    "1. Heridas punzo penetrantes",
    "2. Virus",
    "3. Hemorragia",
    "4. Reacción alérgica",
    "5. Deshidratación"
]


comunas = [
    "Santiago", "Providencia", "Ñuñoa",
    "Maipú", "La Florida", "Las Condes",
    "Macul", "Peñalolén", "La Reina", "Vitacura"
]

def ingresar_nombre_apellido():
    while True:
        try:
            nombre = input("Ingrese su nombre y apellido: ").strip()
            if nombre:
                return nombre
            else:
                print("Por favor, ingrese un caracter válido.")
                continue
        except ValueError:
            print("Ingrese caracteres válidos.")
            continue

def ingresar_rut():
    while True:
        try:
            rut = input("Ingrese su RUT: ").strip()
            if rut:
                return rut
            else:
                print("Por favor, ingrese un caracter válido.")
                continue
        except ValueError:
            print("Ingrese caracteres válidos.")
            continue

def seleccionar_patología():
    while True:
        print("Lista de patalogías: ")
        print(*patologías, sep="\n")
        try:
            op = int(input("Elija una opción (1-5): "))
            if 1 <= op <= len(patologías):
                return patologías[op-1]
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Ingrese un número del 1 al 5.")

def ingresar_comuna():
    while True:
        try:
            com = input("Ingrese su comuna: ").strip().title()
            if com in comunas:
                return com
            else:
                print("Comuna no válida. Diríjase a su región.")
        except ValueError:
            print("Ingrese caracteres válidos.")

def registrar_paciente():
    print("\n--- Registro de Paciente ---")
    rut      = ingresar_rut()
    nombre   = ingresar_nombre_apellido()
    patología = seleccionar_patología()
    comuna   = ingresar_comuna()
    
    print("\nPaciente registrado:")
    print(f" RUT: {rut}")
    print(f" Nombre: {nombre}")
    print(f" Patología: {patología}")
    print(f" Comuna: {comuna}\n")

def menú_principal():
    while True:
        print("1. Registrar paciente")
        print("2. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            registrar_paciente()
        elif op == "2":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.\n")

# Inicio del programa
menú_principal()
