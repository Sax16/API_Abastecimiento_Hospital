from fastapi import FastAPI
from routes.asistente import asistente
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API para Gestion de Medicamentos y Equipos",
    description="Esta API está echa para la gestion de medicamentos y equipos médicos de un hospital grande como el de Essalud",
)

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(asistente)