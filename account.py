def gestionar_responsables():
    while True:
        print("Menú Responsables")
        print("1. Ingresar nuevo responsable")
        print("2. Actualizar información de un responsable")
        print("3. Buscar un responsable")
        print("4. Ver información de todos los responsables")
        print("5. Eliminar un responsable")
        print("6. Volver al menú principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ingresar_responsable()
        elif opcion == "2":
            actualizar_responsable()
        elif opcion == "3":
            buscar_responsable()
        elif opcion == "4":
            ver_informacion_todosresponsables()
        elif opcion == "5":
            eliminar_responsable()
        elif opcion == "6":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Error, ingrese una opción válida.")

def ingresar_responsable():
    while True:
        codigo_responsable = input("Crea el código del responsable del equipo (Debe tener entre 4 y 6 caracteres, sólo números): ")
        a = len(codigo_responsable)
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (a <= 6 and a >= 4) :
            break
        else:
            print("El código del responsable no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 4 carácteres o más de 6. Inténtelo nuevamente.")
    while True:
        nombre = input("Ingrese el nombre del responsable: ")
        if nombre.strip() and nombre.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        nombre = input("Ingrese el nombre del responsable: ")
        if nombre.strip() and nombre.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    
    while True:
        apellido = input("Ingrese el apellido del responsable: ")
        if apellido.strip() and apellido.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    
    while True:
        num_documento = int(input("Ingrese el número del documento de identidad: "))
        a = len(codigo_responsable)
        if num_documento.strip() and num_documento.isnumeric() and (a <= 9 and a >= 10) :
            break
        else:
            print("El documento del responsable no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 9 carácteres o más de 10. Inténtelo nuevamente.")
    
    while True:
        cargo = input("Ingrese el cargo del responsable: ")
        if cargo.strip() and cargo.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
