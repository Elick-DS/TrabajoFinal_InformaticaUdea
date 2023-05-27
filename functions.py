def ingresar_equipo():
    while True:
        serial = input("Ingrese el número de serie: ")
        if serial.strip() and serial.isalnum() and len(serial) == 10:
            break
        else:
            print("El número de serie no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 10 caracteres. Inténtelo nuevamente.")
    while True:
        numero_activo = input("Ingrese el número de activo: ")
        if numero_activo.strip() and numero_activo.isnumeric() and len(numero_activo) == 4:
            break
        else:
            print("El número de activo no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")
    while True:
        nombre_equipo = input("Ingrese el número de equipo: ")
        if nombre_equipo.strip() and nombre_equipo.isalpha():
            break
        else:
            print("El nombre de equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
    marca = input("Ingrese la marca del equipo: ")
    codigo_ubicacion = int(input("Ingrese el código de ubicación del equipo: "))
    codigo_responsable = int(input("Ingrese el código del responsable del equipo: "))

def ingresar_responsable():
    codigo_responsable = int(input("Ingrese el código del responsable: "))
    nombre = input("Ingrese el nombre del responsable: ")
    apellido = input("Ingrese el apellido del responsable: ")
    num_documento = int(input("Ingrese el número del documento de identidad: "))
    cargo = input("Ingrese el cargo del responsable: ")

def ingresar_ubicacion():
    codigo_ubicacion = int(input("Ingrese el código de ubicación: "))
    nombre_ubicacion = input("Ingrese el nombre de la ubicación: ")
    piso = int(input("Ingrese el número de piso: "))

def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Gestionar información equipos")
        print("2. Gestionar información responsables")
        print("3. Gestionar información ubicaciones")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_equipos()
        elif opcion == "2":
            menu_responsables()
        elif opcion == "3":
            menu_ubicaciones()
        elif opcion == "4":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Error, ingrese una opción válida.")

    