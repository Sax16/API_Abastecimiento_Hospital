from fastapi import FastAPI
from routes.asistente import asistente

app = FastAPI(
    title="API para Gestion de Medicamentos y Equipos",
    description="Esta API está echa para la gestion de medicamentos y equipos médicos de un hospital grande como el de Essalud",
)

app.include_router(asistente)