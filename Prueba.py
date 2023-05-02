class Fecha:
    def __init__ (self, año:int=2023, mes:int=5, dia:int=2):
        self.año=año
        self.mes=mes
        self.dia=dia
    def __repr__(self) -> str:
        return f'Fecha=año={self.año}, mes={self.mes}, dia={self.dia}'
class Persona:
    def __init__ (self, nombre: str, apellido: str, nacimiento: Fecha):
        self.nombre= nombre
        self.apellido= apellido
        self.nacimiento=nacimiento
    def __repr__(self) -> str:
       return f'Persona=nombre={self.nombre}, apellido={self.apellido}, nacimiento={self.nacimiento}'

if __name__== "__main__":
    persona=Persona (nombre= "Peter", apellido= "Parker", nacimiento=Fecha(año=1999, mes=12, dia=15))
    print (persona)