from data_base import ingresar_equipo_manual, buscar_equipo,eliminar_equipo, actualizar_equipo, ingresar_equipos_automaticamente, ver_equipos
from account import gestionar_responsables

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
            gestionar_responsables()
        elif opcion == "3":
            menu_ubicaciones()
        elif opcion == "4":
            print("¡Gracias por utilizar el sistema!")
            exit()
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
            ingresar_equipos_automaticamente()
        elif opcion == "3":
            actualizar_equipo()
        elif opcion == "4":
            buscar_equipo()
        elif opcion == "5":
            ver_equipos()
        elif opcion == "6":
            eliminar_equipo()
        elif opcion == "7":
            break
        else:
            print("Error, ingrese una opción válida")





def menu_ubicaciones():
    while True:
     print("Menú Ubicaciones")
     print("1. Ingresar nueva ubicación")
     print("2. Actualizar información de una ubicación")
     print("3. Buscar una ubicación")
     print("4. Ver información de todas las ubicaciones")
     print("5. Eliminar una ubicación")
     print("6. Volver al menú principal")
    
     opcion = input("Selecciona una opción: ")

#      if opcion == "1":
#             ingresar_nueva_ubicacion()
#      elif opcion == "2":
#             actualizar_ubicacion()
#      elif opcion == "3":
#             buscar_ubicacion()
#      elif opcion == "4":
#             ver_informacion_todasubicaciones()
#      elif opcion == "5":
#             eliminar_ubicacion()
#      elif opcion == "6":
#             print("¡Gracias por utilizar el sistema!")
#             break
#      else:
#             print("Error, ingrese una opción válida.")





    