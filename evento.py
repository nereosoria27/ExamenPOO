from main import Evento

class Examen():
    def __init__(self, nombre, fecha):
        self._nombre = nombre
        self._fecha = fecha

    def __str__(self):
        return f"Nombre: {self._nombre}\nFecha: {self._fecha}"