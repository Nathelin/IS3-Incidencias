from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from api.evento import Evento
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/eventos/", response_model=Evento)
def crear_evento(evento: Evento):
    with Session(engine) as session:
        session.add(evento)
        session.commit()
        session.refresh(evento)
        return evento

@app.get("/eventos/", response_model=list[Evento])
def listar_eventos():
    with Session(engine) as session:
        eventos = session.exec(select(Evento)).all()
        return eventos
    
# fin