from evento import Evento
class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, materia, entrega):
        super().__init__(fecha, descripcion)
        self.materia = materia
        self.entrega = entrega
    
    def __str__(self):
        return f"Trabajo Práctico de {self.materia} - Entrega: {self.entrega} - {super().__str__()}"