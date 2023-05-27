def ingresar_equipo():
    while True:
        serial = input("Ingrese el número de serie: ")
        if serial.strip() and serial.isalnum() and len(serial) == 10:
            break
        else:
            print("El número de serie no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")
    while True:
        numero_activo = input("Ingrese el número de serie: ")
        if numero_activo.strip() and numero_activo.isnumeric() and len(numero_activo) == 4:
            break
        else:
            print("El número de serie no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")
    nombre_equipo = input("Ingrese el nombre del equipo: ")
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
    