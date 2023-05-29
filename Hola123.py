
import csv

def ingreso_automatico_equipos():
    archivo_csv = input("Aqui va el nombre del archivo CSV:")
    
    with open(archivo_csv, newline='') as csvfile:
        equipos_csv = csv.DictReader(csvfile)
        for equipo in equipos_csv:
            equipos_collection.insert_one(equipo)
    
    print("Ingreso satisfactorio.")


def ver_equipos():
    equipos = equipos_collection.find()
    if equipos.count() > 0:
        print("Equipos registrados:")
        for equipo in equipos:
            print(f"Serial: {equipo['serial']}")
            print(f"Número de activo: {equipo['numero_activo']}")
            print(f"Nombre: {equipo['nombre']}")
            print(f"Marca: {equipo['marca']}")
            print(f"Código de ubicación: {equipo['codigo_ubicacion']}")
            print(f"Código de responsable: {equipo['codigo_responsable']}")
            print("----------")
    else:
        print("No hay equipos registrados.")





