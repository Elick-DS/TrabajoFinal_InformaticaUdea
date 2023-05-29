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
            ingresar_nuevo_responsable()
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
