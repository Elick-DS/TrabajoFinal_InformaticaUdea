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

def menu_equipos():
    while True:
        print("Menú equipos")
        print("1. Ingresar un nuevo equipo en forma manual")
        print("2. Ingresar un nuevo equipo en forma automática")
        print("3. Actualizar la información de un equipo (por número de activo)")
        print("4. Buscar un equipo (por número de activo)")
        print("5. Ver la información de todos los equipos almacenados")
        print("6. Eliminar un equipo (por número de activo)")
        print("7. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ingresar_equipo_manual()
        elif opcion == "2":
            ingresar_equipo_automatico()
        elif opcion == "3":
            actualizar_equipo()
        elif opcion == "4":
            buscar_equipo()
        elif opcion == "5":
            mostrar_equipos()
        elif opcion == "6":
            eliminar_equipo()
        elif opcion == "7":
            break
        else:
            print("Error, ingrese una opción válida")


def ingresar_equipo_automatico():
    print("Ingresar equipo de forma automática")
    equipos_csv = cargar_equipos_desde_csv()
    for equipo_csv in equipos_csv:
        equipo_obj = equipo.from_csv(equipo_csv)
        agregar_equipo(equipo_obj)
    print("Equipos agregados exitosamente.")

def actualizar_equipo():
    print("Actualizar la información de un equipo específico")
    num_activo = int(input("Ingresa el número de activo del equipo a actualizar: "))
    equipo_obj = obtener_equipo_por_numero_activo(num_activo)

    if equipo_obj:
        print("Equipo encontrado. Ingresa los datos a actualizar:")
        try:
            serial = input(f"Serial ({equipo_obj.serial}): ")
            nombre = input(f"Nombre del equipo ({equipo_obj.nombre}): ")
            marca = input(f"Marca ({equipo_obj.marca}): ")
            cod_ubicacion = int(input(f"Código de ubicación ({equipo_obj.cod_ubicacion}): "))
            cod_responsable = int(input(f"Código de responsable ({equipo_obj.cod_responsable}): "))

            equipo_obj.serial = serial if serial else equipo_obj.serial
            equipo_obj.nombre = nombre if nombre else equipo_obj.nombre
            equipo_obj.marca = marca if marca else equipo_obj.marca
            equipo_obj.cod_ubicacion = cod_ubicacion if cod_ubicacion else equipo_obj.cod_ubicacion
            equipo_obj.cod_responsable = cod_responsable if cod_responsable else equipo_obj.cod_responsable

            actualizar_equipo(equipo_obj)
            print("El equipo se actualizó satisfactoriamente.")
        except ValueError:
            print("Error, solo se pueden ingresar valores numéricos.")
    else:
        print("Equipo no encontrado.")

def menu_responsables():
    pass

def menu_ubicaciones():
    pass

def main():
    menu_principal()

if __name__ == "__main__":
    main()






