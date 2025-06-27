def ingresar_nombre():
    while True:
        nombre=input("Ingrese su nombre")
        if nombre:
            return nombre
        else:
            print("Por favor, ingrese caracteres valido")

def ingresar_rut():
    while True:
        try:
            rutu=int(input("Ingrese su rut"))
            if rutu:
                return rutu
            else:
                print("Por favor, ingrese solo digitos")
        except ValueError:
            print("Por favor, ingrese un caracter valido")

def seleccionar_servicio():
      while True:
        print("\nSeleccione servicio:")
        print("1. Frenos y engrasado")
        print("2. Lavado")
        print("3. Pintura")
        print("4. Especial (todo incluido)")
        print("5. Salir")
        try:
            op = int(input("Opción (1-5): ").strip())
            if 1 <= op <= 5:
                return op
            print("Opción fuera de rango, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def seleccionar_ubicacion():
    while True:
        print("\nSeleccione ubicación:")
        print("1. Concepción")
        print("2. Puente Alto")
        print("3. Muelle Varón")
        print("4. Muelle Vergara")
        print("5. Volver al menú principal")
        try:
            op = int(input("Opción (1-5): ").strip())
            if 1 <= op <= 5:
                return op
            print("Opción fuera de rango, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def procesar_servicio():
    print("\n--- Gestión de Servicio ---")
    nombre = ingresar_nombre()
    rut    = ingresar_rut()
    servicio = seleccionar_servicio()
    if servicio == 5:
        return  # vuelve al menú principal sin hacer nada
    ubicacion = seleccionar_ubicacion()
    if ubicacion == 5:
        return  # vuelve al menú principal

    servicios = {
        1: "Frenos y engrasado",
        2: "Lavado",
        3: "Pintura",
        4: "Especial (todo incluido)"
    }
    ubicaciones = {
        1: "Concepción",
        2: "Puente Alto",
        3: "Muelle Varón",
        4: "Muelle Vergara"
    }

    print("\n--- Ticket de Servicio ---")
    print(f"RUT:       {rut}")
    print(f"Nombre:    {nombre}")
    print(f"Servicio:  {servicios[servicio]}")
    print(f"Ubicación: {ubicaciones[ubicacion]}")


procesar_servicio()
