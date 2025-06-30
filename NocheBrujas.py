compradores = []

def ingresar_nombre():
    while True:
        n = input("Ingrese nombre del comprador: ").strip()
        if n:
            return n

def ingresar_tipo_entrada():
    while True:
        t = input("Tipo de entrada (general/vip): ").strip().lower()
        if t in ("general", "vip"):
            return t.title()
        print("Debe ser 'general' o 'vip'")

def ingresar_codigo_confirmacion():
    while True:
        c = input("Código de confirmación: ").strip()
        if len(c) >= 6 and any(ch.isdigit() for ch in c) and " " not in c:
            return c
        print("Mínimo 6 caracteres, al menos un número y sin espacios")

def comprar_entrada():
    nombre = ingresar_nombre()
    for c in compradores:
        if c["nombre"] == nombre:
            print("Ese nombre ya tiene una compra registrada")
            return
    tipo = ingresar_tipo_entrada()
    codigo = ingresar_codigo_confirmacion()
    compradores.append({
        "nombre": nombre,
        "tipo": tipo,
        "codigo": codigo
    })
    precio = 10000 if tipo == "General" else 50000
    print(f"Compra exitosa: {nombre} - {tipo} (${precio}) - Cód. {codigo}")

def consultar_comprador():
    nombre = ingresar_nombre()
    for c in compradores:
        if c["nombre"] == nombre:
            print(f"Nombre: {c['nombre']}")
            print(f"Tipo: {c['tipo']}")
            print(f"Código: {c['codigo']}")
            return
    print("Comprador no existe")

def cancelar_compra():
    nombre = ingresar_nombre()
    for c in compradores:
        if c["nombre"] == nombre:
            compradores.remove(c)
            print(f"Compra de {nombre} cancelada")
            return
    print("Comprador no existe")

def continuar_o_salir():
    resp = input("¿Desea continuar? (s/n): ").strip().lower()
    return resp == "s"

def menu():
    while True:
        print("""
--- MENÚ CONCIERTO ---
1. Comprar entrada
2. Consultar comprador
3. Cancelar compra
4. Continuar o salir""")
        opc = input("Elige (1-4): ").strip()
        if opc == "1":
            comprar_entrada()
        elif opc == "2":
            consultar_comprador()
        elif opc == "3":
            cancelar_compra()
        elif opc == "4":
            if not continuar_o_salir():
                break
        else:
            print("Opción inválida")

menu()