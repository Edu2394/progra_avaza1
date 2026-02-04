class persona():
    lista=[]
    def __init__(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo
    def registrar(self):
        persona.lista.append(self)
        print(f"La persona {self.nombre} ha sido registrada con el correo {self.correo}")
    def actualizar_datos(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo
        print(f"Los datos ha sido actualizados")
    @classmethod
    def personas_registradas(cls):
        print(f"Personas registradas")
        for x in cls.lista:
            print(f"-{x.nombre} - {x.correo}")
