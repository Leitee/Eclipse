'''
Created on 12/5/2015

@author: leonardo
'''
from Alumno import *
op = "S"

while op.upper() == "S":
    cargarAlumno()
    op = input("Desea seguir cargando alumnos? (S/N): ")

print("\n")
   
while True:
    try:
        accion = int(input("Que tipo de busqueda dese hacer? 1(Por Apellido) 2(Por Sexo) 3(Por Edad): "))
        break
    except:
        print("Error de formato invalido.")
        
if accion == 1:
    buscarPorNombre()
elif accion == 2:
    buscarPorSexo()
elif accion == 3:
    buscarPorEdad()
    