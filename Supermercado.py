productos = [
    "1.-Leche $1000",
    "2.-Pan $1500",
    "3.-Huevos $2700",
    "4.-Tallarines $1300",
    "5.-Azucar $1400"
]
stock = [10, 20, 12, 15, 8]

def ingresar_nombre():
    while True:
        n = input("Ingresa tu nombre: ")
        if n:
            return n

def ingresar_direccion():
    while True:
        d = input("Ingresa tu dirección: ")
        if d:
            return d

def ingresar_rut():
    while True:
        try:
            r = int(input("Ingresa tu rut: "))
            if r:
                return r
        except ValueError:
            pass

def venta_productos():
    print("Por favor, ingresa tus datos:")
    u = ingresar_nombre()
    _ = ingresar_direccion()
    _ = ingresar_rut()
    print("\nProductos disponibles:")
    print(*productos, sep="\n")
    carrito = []
    cods = input("\nCódigos separados por espacio (ej: 1 3 5): ").split()
    for c in cods:
        i = int(c) - 1
        if 0 <= i < len(productos) and stock[i] > 0:
            stock[i] -= 1
            carrito.append(productos[i])
    print(f"\nCarrito de {u}:")
    for p in carrito:
        print("-", p)

def devolucion_productos():
    print("\nDevolución de productos:")
    print(*productos, sep="\n")
    cods = input("\nCódigos a devolver separados por espacio: ").split()
    for c in cods:
        i = int(c) - 1
        if 0 <= i < len(productos):
            stock[i] += 1
    print("\nInventario tras devolución:")
    for p, s in zip(productos, stock):
        print(f"{p} - stock {s}")

def menu_principal():
    while True:
        print("\n1.-Venta de productos")
        print("2.-Devolución de productos")
        print("3.-Mostrar inventario")
        print("4.-Salir")
        o = int(input("Opción (1-4): "))
        if o == 1:
            venta_productos()
        elif o == 2:
            devolucion_productos()
        elif o == 3:
            print("\nInventario actual:")
            for p, s in zip(productos, stock):
                print(f"{p} - stock {s}")
        elif o == 4:
            break

menu_principal()