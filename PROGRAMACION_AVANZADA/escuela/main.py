from escuela import Alumno,Grupo

alumno1=Alumno("Caro Sanchez",23345)
alumno2=Alumno("Eduardo Gomez",3557)
alumno3=Alumno("Beto",22222)
alumno4=Alumno("Gabriel Itzcoatl",2222)
alumno5=Alumno("Santiago Hernández",3227)


alumno1.agregar_calificacion(9.5)
alumno1.agregar_calificacion(9.5)
alumno1.agregar_calificacion(9)

alumno2.agregar_calificacion(9.5)
alumno2.agregar_calificacion(9.5)

alumno3.agregar_calificacion(6)
alumno3.agregar_calificacion(5)
alumno3.agregar_calificacion(7)
alumno3.agregar_calificacion(8)

alumno4.agregar_calificacion(9.5)
alumno4.agregar_calificacion(9)
alumno4.agregar_calificacion(7)

alumno5.agregar_calificacion(7)
alumno5.agregar_calificacion(8)
alumno5.agregar_calificacion(7)


print(f"La alumna {alumno1.nombre} tiene pormedio de: {alumno1.calcular_promedio():.2f} y esta: {alumno1.estado_final()}")
print(f"El alumno {alumno2.nombre} tiene pormedio de: {alumno2.calcular_promedio():.2f} y esta: {alumno2.estado_final()}")
print(f"El alumno {alumno3.nombre} tiene pormedio de: {alumno3.calcular_promedio():.2f} y esta: {alumno3.estado_final()}")
print(f"El alumno {alumno4.nombre} tiene pormedio de: {alumno4.calcular_promedio():.2f} y esta: {alumno4.estado_final()}")
print(f"El alumno {alumno5.nombre} tiene pormedio de: {alumno5.calcular_promedio():.2f} y esta: {alumno5.estado_final()}")

grupo1=Grupo("Progra")
grupo1.agregar_alumno(alumno1)
grupo1.agregar_alumno(alumno2)
grupo1.agregar_alumno(alumno3)
grupo1.agregar_alumno(alumno4)
grupo1.agregar_alumno(alumno5)

grupo1.mostrar_promedios()
grupo1.mejor_alumno()