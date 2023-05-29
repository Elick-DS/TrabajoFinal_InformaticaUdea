from functions import  menu_principal
from data_base import ingresar_equipo_manual

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
myres = mydb["responsables"]

print("BIENVENIDO A NUESTRO SISTEMA DE CONTROL DE INVENTARIOS MÉDICOS")

while True:
    opcion = input("1.Inciar sesión\n2.Crearse una cuenta")
    if opcion.isnumeric() and opcion == 1 or opcion == 2:
        break
    else:
        print("Ingresa una opción correcta")

if opcion == 1:
        code = input("Ingresa el número de activo: ")
        for y in myres.find({'numero_activo': code}):
             print(f"Usuario {y['nombre']}")

menu_principal()
