class Agenda:
    def __init__(self):
        self.eventos = []
    
    def agregar_evento(self, evento):
        self.eventos.append(evento)
    
    def mostrar_eventos(self):
        for evento in self.eventos:
            print(evento)
    
    def eliminar_evento(self, descripcionE):
        
        descripcionE = input("Ingresa la descripción del evento que quiere eliminar: ")
        for evento in self.eventos:
            if evento.descripcion == descripcionE:
                self.eventos.remove(evento)