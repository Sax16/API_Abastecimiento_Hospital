from fastapi import APIRouter, Form
from config.db import conn
from models.asistente import asistentes
from schemas.asistente import Asistente


asistente = APIRouter()

# Para obtener todos los empleados de la base de datos
@asistente.get("/asistentes", tags=['asistentes'])
def get_asistentes():
    return conn.execute(asistentes.select()).fetchall()


# Para crear nuevos registros de empleados
@asistente.post("/asistentes", tags=["asistentes"])
async def crear_asistente(
    asiRUC: str = Form(...),
    asiNombres: str = Form(...),
    asiApPaterno: str = Form(...),
    asiApMaterno: str = Form(...),
    asiGenero: str = Form(...),
    asiTelefono: str = Form(...),
    asiEmail: str = Form(...)
):
    # Creamos el diccionario para nuestro empleado
    nuevo_empleado = {
        "asiRUC": asiRUC,
        "asiNombres": asiNombres,
        "asiApPaterno": asiApPaterno,
        "asiApMaterno": asiApMaterno,
        "asiGenero": asiGenero,
        "asiTelefono": asiTelefono,
        "asiEmail": asiEmail
    }

    # Insertamos los datos a la base de datos
    resultado = conn.execute(asistentes.insert().values(nuevo_empleado))

    valores = resultado.last_inserted_params()

    #Retornamos el usuario creado
    conn.execute(asistentes.select().where(asistentes.c.asiRUC == valores['asiRUC'])).first()

@asistente.get("/asistentes/{ruc}", tags=["asistentes"])
def get_asistente(ruc: str):
    return conn.execute(asistentes.select().where(asistentes.c.asiRUC == ruc)).first()