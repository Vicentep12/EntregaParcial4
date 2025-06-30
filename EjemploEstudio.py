carreras = ["1.-Ingenería", "2.-Analista", "3.-Gastronomía"]
modulo_ingenería    = ["1.-Desarrollo Web", "2.-Desarrollo Móvil", "3.-Escritorio"]
modulo_analista     = ["1.-Análisis de Datos", "2.-Limpieza de Datos", "3.-Dashboards"]
modulo_gastronomia  = ["1.-Historia", "2.-Alimentos Naturales", "3.-Sopaipillas"]

lista_estudiantes = []

def ingresar_nombre():
    while True:
        n = input("Ingrese su nombre: ").strip()
        if n:
            return n

def ingresar_rut():
    while True:
        try:
            r = int(input("Ingrese su rut: "))
            if r:
                return r
            else:
                print("Por favor, ingrese su rut")
        except ValueError:
            print("Por favor, use caracteres válidos")

def ingresar_correo():
    while True:
        c = input("Ingrese su correo electrónico: ").strip()
        if c:
            return c

def registrar_estudiante():
    nombre   = ingresar_nombre()
    rut      = ingresar_rut()
    correo   = ingresar_correo()

    print("\nA continuación por favor seleccione su carrera:")
    print(*carreras, sep="\n")
    op1 = int(input("Seleccione carrera (1-3): "))

    carrera     = ""
    especialidad = ""

    if op1 == 1:
        print("Su carrera elegida fue Ingeniería.")
        print("\nSus especialidades son:")
        print(*modulo_ingenería, sep="\n")
        op2 = int(input("Seleccione aquí: "))
        if op2 == 1:
            print("Su especialización fue Desarrollo Web")
            especialidad = "Desarrollo Web"
        elif op2 == 2:
            print("Su especialización fue Desarrollo Móvil")
            especialidad = "Desarrollo Móvil"
        elif op2 == 3:
            print("Su especialización fue Escritorio")
            especialidad = "Escritorio"
            carrera = "Ingeniería"

    if op1 == 2:
        print("Su carrera elegida fue Analista.")
        print("\nSus especialidades son:")
        print(*modulo_analista, sep="\n")
        op2 = int(input("Seleccione aquí: "))
        if op2 == 1:
            print("Su especialización fue Análisis de Datos")
            especialidad = "Análisis de Datos"
        elif op2 == 2:
            print("Su especialización fue Limpieza de Datos")
            especialidad = "Limpieza de Datos"
        elif op2 == 3:
            print("Su especialización fue Dashboards")
            especialidad = "Dashboards"
            carrera = "Analista"

    if op1 == 3:
        print("Su carrera elegida fue Gastronomía.")
        print("\nSus especialidades son:")
        print(*modulo_gastronomia, sep="\n")
        op2 = int(input("Seleccione aquí: "))
        if op2 == 1:
            print("Su especialización fue Historia")
            especialidad = "Historia"
        elif op2 == 2:
            print("Su especialización fue Alimentos Naturales")
            especialidad = "Alimentos Naturales"
        elif op2 == 3:
            print("Su especialización fue Sopaipillas")
            especialidad = "Sopaipillas"
            carrera = "Gastronomía"

    estudiante = {
        "nombre":       nombre,
        "rut":          rut,
        "correo":       correo,
        "carrera":      carrera,
        "especialidad": especialidad
    }
    lista_estudiantes.append(estudiante)
    print(f"\nEstudiante {nombre} (RUT {rut}) registrado con éxito.\n")


def eliminar_estudiante():
    try:
        rut_elim = int(input("Ingrese el RUT del estudiante a eliminar: "))
    except ValueError:
        print("Rut inválido. Usa sólo números.")
        return
    
    estudiantes_borrar= None
    for est in lista_estudiantes:
        if est["rut"] == rut_elim:
            estudiantes_borrar = est
            break

    if estudiantes_borrar:
        lista_estudiantes.remove(estudiantes_borrar)
        print(f"Eliminado: {estudiantes_borrar['nombre']} (RUT {rut_elim})")
    else:
        print(f" No existe ningún estudiante con RUT {rut_elim}.")

def listar_estudiantes():
        if not lista_estudiantes:
                print("— No hay estudiantes registrados —")
        else:
            for e in lista_estudiantes:
                    print(f"{e["nombre"]} | {e["rut"]} | {e["carrera"]} - {e["especialidad"]}")




def menu():
    while True:
        print("""\n--- MENÚ ---
1. Registrar estudiante
2. Eliminar estudiante
3. Listar estudiantes
4. Salir""")
        opc = input("Elige (1-4): ")
        if opc == "1":
            registrar_estudiante()
        elif opc == "2":
            eliminar_estudiante()
        elif opc == "3":
            listar_estudiantes()
        elif opc == "4":
            break
        else:
            print("Opción inválida, elige entre 1 y 4.")


menu()