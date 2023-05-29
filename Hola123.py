

# import csv

# def ingreso_automatico_equipos():
#     archivo_csv = input("Aqui va el nombre del archivo CSV:")
    
#     with open("InventarioIPS.csv", 'r') as csvfile:
#         equipos_csv = csv.DictReader(csvfile)
#         for equipo in equipos_csv:
#             mycol.insert_one(equipo)
    
#     print("Ingreso satisfactorio.")

# def actualizar_equipo():
#      numero_activo = input("Ingrese el número de activo del equipo a actualizar: ")
   
#      equipo = mycol.find_one({"numero_activo": numero_activo})
#      if equipo:
#          nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")
#          nuevo_marca = input("Ingrese la nueva marca: ")
#          while True:
#             bloque = input("Ingrese el bloque en el que se encuentra el dispositivo: ")
#             piso = input("Ingresa el piso en el que se encuentra el dispositivo: ")
#             nuevo_bp = f"B{bloque}P{piso}"
#             if nuevo_bp.strip() and nuevo_bp.isalnum():
#                 break
#             else:
#                 print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
#          nuevo_codigo_responsable = input("Ingrese el nuevo código de responsable: ")
       
#          nuevo_equipo = {
#             "$set": {
#                 "nombre": nuevo_nombre,
#                 "marca": nuevo_marca,
#                 "codigo_ubicacion": nuevo_bp,
#                 "codigo_responsable": nuevo_codigo_responsable
#             }
#         }
       
#          mycol.update_one({"numero_activo": numero_activo}, nuevo_equipo)
#          print("Equipo actualizado satisfactoriamente.")
#      else:
#          print("No se encontro el equipo.")




# def ver_equipos():
#     equipos = mycol.find()
#     if equipos.count() > 0:
#         print("Equipos registrados:")
#         for equipo in equipos:
#             print(f"Serial: {equipo['serial']}")
#             print(f"Número de activo: {equipo['numero_activo']}")
#             print(f"Nombre: {equipo['nombre_equipo']}")
#             print(f"Marca: {equipo['marca']}")
#             print(f"Código de ubicación: {equipo['codigo_ubicacion']}")
#             print(f"Código de responsable: {equipo['codigo_responsable']}")
#             print("----------")
#     else:
#         print("No hay equipos registrados.")



# def gestionar_responsables():
#     while True:
#         print("Menú Responsables")
#         print("1. Ingresar nuevo responsable")
#         print("2. Actualizar información de un responsable")
#         print("3. Buscar un responsable")
#         print("4. Ver información de todos los responsables")
#         print("5. Eliminar un responsable")
#         print("6. Volver al menú principal")
    
#         opcion = input("Selecciona una opción: ")

#         if opcion == "1":
#             ingresar_nuevo_responsable()
#         elif opcion == "2":
#             actualizar_responsable()
#         elif opcion == "3":
#             buscar_responsable()
#         elif opcion == "4":
#             ver_informacion_todosresponsables()
#         elif opcion == "5":
#             eliminar_responsable()
#         elif opcion == "6":
#             print("¡Gracias por utilizar el sistema!")
#             break
#         else:
#             print("Error, ingrese una opción válida.")


# def gestionar_ubicaciones():
#     while True:
#      print("Menú Ubicaciones")
#      print("1. Ingresar nueva ubicación")
#      print("2. Actualizar información de una ubicación")
#      print("3. Buscar una ubicación")
#      print("4. Ver información de todas las ubicaciones")
#      print("5. Eliminar una ubicación")
#      print("6. Volver al menú principal")





