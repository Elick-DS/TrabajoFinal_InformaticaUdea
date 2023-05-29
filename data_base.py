from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from functions import input_no_vacio

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










            



