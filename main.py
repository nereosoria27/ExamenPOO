#no funciona todavia, pero yo confio en que lo va a hacer

from evento import Evento
from trabajopractico import TrabajoPractico
from reunionestudio import ReunionEstudio
from examen import Examen

from agenda import Agenda

eventos = []


def mostrar_menu():
    print("1. Agregar evento")
    print("2. Mostrar eventos")
    print("3. Eliminar evento")
    print("4. Salir")

def agregar_evento(agenda):
    tipo_evento = input("Ingrese el tipo de evento (examen, trabajo_practico, reunion_estudio): ")
    fecha = input("Ingrese la fecha del evento (dd/mm/aaaa): ")
    descripcion = input("Ingrese la descripción del evento: ")

    if tipo_evento == "examen":
        materia = input("Ingrese la materia del examen: ")
        evento = Examen(fecha, descripcion, materia)
    elif tipo_evento == "trabajo_practico":
        materia = input("Ingrese la materia del trabajo práctico: ")
        entrega = input("Ingrese la fecha de entrega del trabajo práctico (dd/mm/aaaa hh:mm): ")
        evento = TrabajoPractico(fecha, descripcion, materia, entrega)
    elif tipo_evento == "reunion_estudio":
        tema = input("Ingrese el tema de la reunión de estudio: ")
        evento = ReunionEstudio(fecha, descripcion, tema)
    else:
        print("Tipo de evento no válido.")
        return

    agenda.agregar_evento(evento)
    print("Evento agregado")

def eliminar_evento(agenda, descripcion):
    descripcion = input("Ingresa la descripción del evento que quiere eliminar: ")
    agenda.eliminar_evento(descripcion)
    print("Evento eliminado")

def main():
    agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_evento(agenda)
        elif opcion == "2":
            print("Eventos en la agenda:")
            agenda.mostrar_eventos()
        elif opcion == "3":
            agenda.eliminar_evento(agenda, descripcion)
        elif opcion == "4":

            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()