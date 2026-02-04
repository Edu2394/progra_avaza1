class Animales():
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido(self):
        print("sonido")




class Conejo(Animales):
    def sonido1(self):
         print("Sniff sniff")
    def caract(self):
        print(f"Mi conejo se llama {self.nombre} es color {self.color} y tiene {self.patas} patas")
    
    
class ornitorrinco(Animales):
    def __init__(self,nombre,color,patas,pico):
       super().__init__(nombre,color,patas)
       self.pico=pico
    def sonido2(self):
        print("krrrrrrrrrrrr")
    def caract(self):
        print(f"Mi ornitorrinco se llama {self.nombre} es color {self.color}, tiene {self.patas} patas y mi pico mide {self.pico}")
    
class Dinosaurio(Animales):
    tipo="Dinosaurio"
    def sonido3(self):
        print("Rawr rawr")
    def caract(self):
        print(f"Mi dino se llama {self.nombre} es color {self.color}, tiene {self.patas} patas y soy un {self.tipo}")
    

            