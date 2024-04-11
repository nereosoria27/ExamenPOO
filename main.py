eventos = []

class Evento():
    def __init__(self, fecha, descripcion, examen=None):
        self._fecha = fecha
        self._descripcion = descripcion
        self._examen = examen

    def __str__(self):
        examen_str = f"Examen: {self._examen}" if self._examen else ""
        return f"Fecha: {self._fecha}\nDescripción: {self._descripcion}\n{examen_str}"



def agregar_evento():
    fecha = input("Ingrese la fecha del evento: ")
    descripcion = input("Ingrese la descripcion del evento: ")
    tipo = input("Que evento desea crear (EXAMEN) ")
    if tipo == "EXAMEN":
        nombre = input("Ingrese el nombre del examen: ")
        eventos.append(Evento(fecha, descripcion, Examen(nombre, fecha)))
    else:
        eventos.append(Evento(fecha, descripcion))
    print(eventos)

def eliminar_evento():
    if len(eventos) > 0:
        eventos.pop()
    else:
        print("No hay eventos para eliminar.")
print("AGENDA")


while True:
    print(eventos)
    eleccion = input("Ingrese su eleccion, 1 para añadir 2 para eliminar ")
    if eleccion == "1":
        agregar_evento()
        tipo = input("Que evento desea crear (EXAMEN) ")
        if tipo == "EXAMEN":
            agregar_evento()
    elif eleccion == "2":
        eliminar_evento()
    else:
        print("Elección inválida. Por favor, intente de nuevo.")