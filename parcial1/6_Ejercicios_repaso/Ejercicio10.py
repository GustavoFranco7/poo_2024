#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
reprobados = 0


for i in range(15):
    calificacion = int(input(f"Introduce la calificación del alumno {i+1}: "))
    
    
    if calificacion >= 80:
        aprobados += 1
    else:
        reprobados += 1


print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")