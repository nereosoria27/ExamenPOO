from main import Evento

class ReunionEstudio(Evento):
    def __init__(self, fecha, descripcion, tema):
        super().__init__(fecha, descripcion)
        self.tema = tema
    
    def __str__(self):
        return f"Reunión de Estudio sobre {self.tema} - {super().__str__()}"