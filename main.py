from insertar import registrar_sala, registrar_reserva
from consultar import consultar_salas, consultar_reservas
from eliminar import cancelar_reserva
from conexion import engine
from modelos import Base

Base.metadata.create_all(engine)


def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")


def main():
    while True:
        print("""
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir""")
        opcion = pedir_numero("Opción: ")

        try:
            if opcion == 1:
                nombre = input("Nombre de la sala: ")
                capacidad = pedir_numero("Capacidad: ")
                registrar_sala(nombre, capacidad)
                print("Sala registrada.")
            elif opcion == 2:
                consultar_salas()
            elif opcion == 3:
                estudiante = input("Estudiante: ")
                sala_id = pedir_numero("ID de la sala: ")
                fecha = input("Fecha (AAAA-MM-DD): ")
                registrar_reserva(estudiante, sala_id, fecha)
                print("Reserva registrada.")
            elif opcion == 4:
                consultar_reservas()
            elif opcion == 5:
                id_reserva = pedir_numero("ID de la reserva: ")
                cancelar_reserva(id_reserva)
            elif opcion == 0:
                break
            else:
                print("Opción inválida.")
        except ValueError as error:
            print(f"Error: {error}")



if __name__ == "__main__":
    main()
    