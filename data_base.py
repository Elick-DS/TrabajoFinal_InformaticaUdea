import csv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["informatica1"]
mycol = mydb["Equipos"]
myres = mydb["responsables"]

def ingresar_equipo_manual():
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
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        if nombre_equipo.strip() and nombre_equipo.isalpha():
            break
        else:
            print("El nombre de equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        marca = input("Ingrese la marca del equipo: ")
        if marca.strip() and marca.isalpha():
            break
        else:
            print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        bloque = input("Ingrese el bloque en el que se encuentra el dispositivo: ")
        piso = input("Ingresa el piso en el que se encuentra el dispositivo: ")
        bp = f"B{bloque}P{piso}"
        if bp.strip() and bp.isalnum():
            break
        else:
            print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        codigo_responsable = input("Ingrese el código del responsable del equipo: ")
        a = len(serial)
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (a <= 6 or a >= 4) :
            break
        else:
            print("El código del responsable no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 4 carácteres o más de 6. Inténtelo nuevamente.")
    
   

    nuevo_equipo = {"serial": serial,"numero_activo": numero_activo,"nombre_equipo": nombre_equipo,"marca": marca,"ubicacion":bp,"codigo_responsable": codigo_responsable}

    x=mycol.insert_one(nuevo_equipo)
    print(x.inserted_id)

def buscar_equipo():
    code = input("Ingresa el número de activo: ")
    for y in mycol.find({'numero_activo': code}):
        print(f"+------------------------------------------+\n"
              f"| Serial             | {y['serial']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Numero activo      | {y['numero_activo']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Nombre equipo      | {y['nombre_equipo']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Ubicación          | {y['ubicacion']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Marca              | {y['marca']:<10}          |\n" 
              f"|------------------------------------------|\n"
              f"| Codigo responsable | {y['codigo_responsable']:<10}          |\n"
              f"|------------------------------------------|\n")

def eliminar_equipo():
    while True:
        numero_activo = input("Ingrese el número de activo: ")
        if numero_activo.strip() and numero_activo.isnumeric() and len(numero_activo) == 4:
            break
        else:
            print("El número de activo no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")
    delete_result = mycol.delete_many({"numero_activo": numero_activo})
    print(f"Se eliminaron {delete_result.deleted_count} documentos con el número de activo {numero_activo}.")


ultima_posicion = 0
def ingresar_equipos_automaticamente():
    global ultima_posicion
    print("Ingresar Equipo Automáticamente")
    archivo_csv = "InventarioIPS.csv"

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        Equipos_collection = db.Equipos

        with open(archivo_csv, newline='') as archivo:
            Equipos = csv.DictReader(archivo, delimiter=';')

            for _ in range(ultima_posicion):
                next(Equipos)

            Equipo = next(Equipos, None)
            if Equipo:

                Equipo_doc = {
                "serial": Equipo["serial"],
                "numero_activo": Equipo["numero_activo"],
                "nombre_equipo": Equipo["nombre_equipo"],
                "marca": Equipo["marca"],
                "ubicacion": Equipo["ubicacion"],
                "codigo_responsable": Equipo["codigo_responsable"]
            }

    
                Equipos_collection.insert_one(Equipo_doc)

                print(f"Se ha ingresado el equipo automáticamente: {Equipo['nombre_equipo']}")

                ultima_posicion += 1
            else:
                print("No hay más equipos para ingresar automáticamente.")

    except FileNotFoundError:
        print("El archivo CSV no existe.")
    except Exception as e:
        print(f"Error al ingresar equipo automáticamente: {str(e)}")



def actualizar_equipo():
     numero_activo = input("Ingrese el número de activo del equipo a actualizar: ")
 
     equipo = mycol.find_one({"numero_activo": numero_activo})
     if equipo:
         nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")
         nuevo_marca = input("Ingrese la nueva marca: ")
         while True:
            bloque = input("Ingrese el bloque en el que se encuentra el dispositivo: ")
            piso = input("Ingresa el piso en el que se encuentra el dispositivo: ")
            nuevo_bp = f"B{bloque}P{piso}"
            if nuevo_bp.strip() and nuevo_bp.isalnum():
                break
            else:
                print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
     
         nuevo_equipo = {
            "$set": {
                "nombre_equipo": nuevo_nombre,
                "marca": nuevo_marca,
                "ubicacion": nuevo_bp
            }
        }
     
         mycol.update_one({"numero_activo": numero_activo}, nuevo_equipo)
         print("Equipo actualizado satisfactoriamente.")
     else:
         print("No se encontro el equipo.")


def ver_equipos():
    print("Ver Equipos")

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        Equipos_collection = db.Equipos

        Equipos = Equipos_collection.find()

        for Equipo in Equipos:
            print("serial:", Equipo["serial"])
            print("numero_activo:", Equipo["numero_activo"])
            print("nombre_equipo:", Equipo["nombre_equipo"])
            print("marca:", Equipo["marca"])
            print("ubicacion:", Equipo["ubicacion"])
            print("codigo_responsable:", Equipo["codigo_responsable"])

    except Exception as e:
        print(f"Error al ver los equipos: {str(e)}")






            



