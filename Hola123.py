
# import csv
# def ingresar_equipos_automaticamente():
#     print("----- Ingresar Equipos Automáticamente -----")
#     archivo_csv = "InventarioIPS.csv"

#     try:
        
#         client = MongoClient(uri, server_api=ServerApi('1'))
#         db = client.informatica1


       
#         equipos_collection = db.equipos

#         with open(archivo_csv, newline='') as archivo:
#             reader = csv.DictReader(archivo)

#             for row in reader:
#                 if "Serial" not in row or not row["Serial"]:
#                     continue  

#                 equipo = {
#                     "Serial": row["Serial"],
#                     "Número de activo": int(row.get("Número de activo", 0)),
#                     "Nombre del equipo": row.get("Nombre del equipo", ""),
#                     "Marca": row.get("Marca", ""),
#                     "Código de ubicación": int(row.get("Código de ubicación", 0)),
#                     "Código responsable": int(row.get("Código responsable", 0))
#                 }

#                 equipos_collection.insert_one(equipo)

#             print("Se han ingresado los equipos automáticamente.")
#     except FileNotFoundError:
#         print("El archivo CSV no existe.")
#     except Exception as e:
#         print(f"Error al ingresar equipos automáticamente: {str(e)}")




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





