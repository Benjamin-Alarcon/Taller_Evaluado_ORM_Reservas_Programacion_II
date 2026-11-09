from conexion import Session
from modelos import Sala, Reserva


def cancelar_reserva(id_reserva):
    with Session.begin() as session:
        reserva = session.get(Reserva, id_reserva)
        if reserva is None:
            raise ValueError("La reserva no existe.")
            
        sala = session.get(Sala, reserva.sala_id)
        session.delete(reserva)
        if sala:
            sala.capacidad +=1
            sala.disponible = True
        print(f"Reserva {id_reserva} cancelada. Sala liberada.")
