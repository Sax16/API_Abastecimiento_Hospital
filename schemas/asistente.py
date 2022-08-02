from pydantic import BaseModel, Field
from typing import Optional
from default.genero import Genero

class Asistente(BaseModel):
    ruc: str = Field(
        ...,
        min_length=11,
        max_length=13
    )

    nombres: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    ap_Paterno: str = Field(
        ...,
        min_length=1,
        max_length=35
    )

    ap_Materno: str = Field(
        ...,
        min_length=1,
        max_length=35
    )

    genero: Genero = Field(...)

    telefono: str = Field(
        ...,
        max_length=15
    )

    email: Optional[str] = Field(default=None)