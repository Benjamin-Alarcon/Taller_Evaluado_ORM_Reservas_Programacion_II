from datetime import date
from sqlalchemy import select
from conexion import Session
from modelos import Sala, Reserva
from consultar import consultar_salas


def registrar_sala(nombre, capacidad):
    nombre = nombre.strip()
    with Session() as session:
        salas = session.scalars(select(Sala)).all()
        for sala in salas:
            if nombre == sala.nombre.strip():
                raise ValueError("Ya hay una sala con ese nombre")
    if not nombre:
        raise ValueError("El nombre de la sala no puede estar vacío.")
    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")
    with Session.begin() as session:
        sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(sala)
        return sala.id


def registrar_reserva(estudiante, sala_id, fecha):
    estudiante = estudiante.strip()
    if not estudiante:
        raise ValueError("El nombre del estudiante no puede estar vacío.")
    try:
        date.fromisoformat(str(fecha))
    except ValueError:
        raise ValueError("La fecha debe tener formato AAAA-MM-DD.")
        

    with Session.begin() as session:
        sala = session.get(Sala, sala_id)
        
        if sala is None:
            raise ValueError(f"No existe una sala con ID {sala_id}.")
            
        if not sala.disponible:
            raise ValueError(f"La sala '{sala.nombre}' no está disponible.")
        sala.capacidad -= 1
        reserva = Reserva(estudiante=estudiante, sala_id=sala.id, fecha=str(fecha))
        sala.disponible = False
        session.add(reserva)
        return reserva.id
