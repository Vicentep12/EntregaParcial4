compradores=[

] #nombre COMPRADOR!!

reservas = 20 #CANTIDAD DE STOCK
  
def reservar_zapatillas():
    print("Ingresa tu nombre a continuacion: ")
    ingresar_nombre=input("Nombre: ")
    if ingresar_nombre:
        print("Nombre registrado con exito.")
        print("Ingrese su codigo de reserva")
        codigo=input("\nCodigo: ") 
        if codigo == "EstoyEnListaDeReserva":
            print(f"Reserva ingresada con exito. Quedan pocas reservas! Apurate!")
            compradores.append(ingresar_nombre)
        else:
            print("Codigo de reserva invalido. Reintente")
            reservar_zapatillas()

def buscar_zapatilla():
    nombre2=input("Ingrese su nombre: ")
    if nombre2 in compradores:
        print("\nReserva encontrada exitosamente")
        print(f"Reserva de {nombre2}")
        print("\nDesea añadir una reserva VIP?(Si/No)")
        vip=input("Ingrese aquí: ")
        if vip =="Si":
            print("Reserva VIP ingresada con exito!")
        else:
            print("No ha seleccionado resera VIP")    
    else:
        print("Reserva no encontrada. Por favor, haga su reserva!")
        reservar_zapatillas()    

def cancelar_reserva():
    nombre3=input("Ingrese el nombre que desea eliminar: ")
    if nombre3 in compradores:
        compradores.remove(nombre3)
        print("Reserva cancelada exitosamente")
    else:
        print("Reserva no encontrada. Por favor haga su reserva")    

def menu():
    while True:
        try:
            print("\nBienvenido a Zapatillas Strike. Eliga sus opciones a continuacion!")
            print("")
            print("1.-Reservar Zapatillas")
            print("2.-Buscar Zapatilla Reservada")
            print("3.-Cancelar Reserva Zapatilla")
            print("4.-Salir")
            op = int(input("Ingrese su opcion: "))
            if op == 1:
                reservar_zapatillas() 
            if op == 2:
                buscar_zapatilla()
            if op == 3:
                cancelar_reserva()
            if op == 4:
                print("Programa terminado...")
                exit
                break
            else:
                print("Ingrese una opcion valida!")   
        except ValueError:
            print("Por favor, ingrese una opcion valida!")
            continue    

menu()


