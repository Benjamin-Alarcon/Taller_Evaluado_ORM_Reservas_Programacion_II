from sqlalchemy import select

from conexion import Session
from modelos import Sala, Reserva


def consultar_salas():
    with Session() as session:
        salas = session.scalars(select(Sala)).all()
        if not salas:
            raise ValueError("No hay salas registradas.")
        
        for sala in salas:
            disponible = "Sí" if sala.disponible else "No"
            print(f"------- Sala {sala.nombre} -------\n ID: {sala.id}\n Capacidad: {sala.capacidad}\n Disponible: {disponible}")


def consultar_reservas():
    with Session() as session:
        reservas = session.scalars(select(Reserva)).all()
        if not reservas:
            raise ValueError("No hay reservas registradas.")
        for reserva in reservas:
            print(f" ID: {reserva.id}\n Estudiante: {reserva.estudiante}\n Sala: {reserva.sala.nombre}\n Fecha{reserva.fecha}")


if __name__ == "__main__":
    print("--- Salas ---")
    consultar_salas()
    print("\n--- Reservas ---")
    consultar_reservas()
