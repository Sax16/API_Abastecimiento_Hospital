from fastapi import APIRouter
from config.db import conn
from models.asistente import asistente
from schemas.asistente import Asistente


asistente = APIRouter()

@asistente.get("/asistentes", response_model=list[Asistente], tags=['asistentes'])
def get_asistentes():
    return conn.execute(asistente.select()).fetchall()