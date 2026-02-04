from animales_clase import *
conejo1=Conejo("Pepe","Blanco",4)
conejo2=Conejo("Beto","Negro",4)

ornitorrinco1=ornitorrinco("Perry","Azul",4,32)
ornitorrinco2=ornitorrinco("Tristan","Negro",4,5)

dinosaurio1=Dinosaurio("trex","Blanco",4)
dinosaurio2=Dinosaurio("raptor","Negro",4)



print(conejo1.nombre)
conejo1.sonido1()
conejo1.caract()

print(conejo2.color)
conejo2.sonido1()
conejo2.caract()

print(ornitorrinco1.nombre)
ornitorrinco1.sonido2()
ornitorrinco1.caract()

print(ornitorrinco2.pico)
ornitorrinco2.sonido2()
ornitorrinco2.caract()

print(dinosaurio1.nombre)
dinosaurio1.sonido3()
dinosaurio1.caract()

print(dinosaurio1.color)
dinosaurio2.sonido3()
dinosaurio2.caract()