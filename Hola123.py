
# import csv

# def ingreso_automatico_equipos():
#     archivo_csv = input("Aqui va el nombre del archivo CSV:")
    
#     with open(archivo_csv, newline='') as csvfile:
#         equipos_csv = csv.DictReader(csvfile)
#         for equipo in equipos_csv:
#             equipos_collection.insert_one(equipo)
    
#     print("Ingreso satisfactorio.")

# def actualizar_equipo():
#     numero_activo = input("Ingrese el número de activo del equipo a actualizar: ")
    
#     equipo = equipos_collection.find_one({"numero_activo": numero_activo})
#     if equipo:
#         nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")
#         nuevo_marca = input("Ingrese la nueva marca: ")
#         nuevo_codigo_ubicacion = input("Ingrese el nuevo código de ubicación: ")
#         nuevo_codigo_responsable = input("Ingrese el nuevo código de responsable: ")
        
#         nuevo_equipo = {
#             "$set": {
#                 "nombre": nuevo_nombre,
#                 "marca": nuevo_marca,
#                 "codigo_ubicacion": nuevo_codigo_ubicacion,
#                 "codigo_responsable": nuevo_codigo_responsable
#             }
#         }
        
#         equipos_collection.update_one({"numero_activo": numero_activo}, nuevo_equipo)
#         print("Equipo actualizado satisfactoriamente.")
#     else:
#         print("No se encontro el equipo.")


# def ver_equipos():
#     equipos = equipos_collection.find()
#     if equipos.count() > 0:
#         print("Equipos registrados:")
#         for equipo in equipos:
#             print(f"Serial: {equipo['serial']}")
#             print(f"Número de activo: {equipo['numero_activo']}")
#             print(f"Nombre: {equipo['nombre']}")
#             print(f"Marca: {equipo['marca']}")
#             print(f"Código de ubicación: {equipo['codigo_ubicacion']}")
#             print(f"Código de responsable: {equipo['codigo_responsable']}")
#             print("----------")
#     else:
#         print("No hay equipos registrados.")





