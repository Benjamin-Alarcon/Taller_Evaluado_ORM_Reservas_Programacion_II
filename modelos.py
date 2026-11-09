from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = "Sala"
    __table_args__ = (
        CheckConstraint("capacidad > 0", name="ck_capacidad"),
    )
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    capacidad = Column(Integer, nullable=False)
    disponible = Column(Boolean, insert_default=True)

    reservas = relationship("Reserva", back_populates="sala")


class Reserva(Base):
    __tablename__ = "Reserva"

    id = Column(Integer, primary_key=True, nullable=False)
    estudiante = Column(String(100), nullable=False)
    sala_id = Column(Integer, ForeignKey("Sala.id"), nullable=False)
    fecha = Column(String(10), nullable=False)

    sala = relationship("Sala", back_populates="reservas")
