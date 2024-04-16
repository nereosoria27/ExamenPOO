from evento import Evento

class Examen(Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia
    
    def __str__(self):
        return f"Examen de {self.materia} - {super().__str__()}"