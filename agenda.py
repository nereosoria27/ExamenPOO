class Agenda:
    def __init__(self):
        self.eventos = []
    
    def agregar_evento(self, evento):
        self.eventos.append(evento)
    
    def mostrar_eventos(self):
        for evento in self.eventos:
            print(evento)
    
    def eliminar_evento(self, descripcion):
        self.eventos = [evento, evento, self.eventos, evento.descripcion, descripcion]