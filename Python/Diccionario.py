'''
Created on 11/5/2015

@author: leonardo
'''

def cargarDatos():
    for i in range(3):
        nombres[i] = input("Ingrese el nombre: ")
        apellidos[i] = input("Ingrese el apellido: ")
        edades[i] = input("Ingrese la edad: ")
        
        

nombres = dict()
apellidos = dict()
edades = dict()
alumnos = list()

cargarDatos()

print()