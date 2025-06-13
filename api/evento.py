import django
from sqlmodel import SQLModel, Field


class Evento(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio: float = Field(default=0.0)
