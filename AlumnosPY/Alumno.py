'''
Created on 12/5/2015

@author: leonardo
'''

alumno = dict()
alumnos = list()

def cargarAlumno():
    while True:
        try:
            alumno["nombre"] = input("Ingrese el nombre: ")
            alumno["apellido"] = input("Ingrese el apellido: ")
            alumno["edad"] = int(input("Ingrese la edad: "))
            alumno["sexo"] = input("Ingrese el sexo. (M/F): ")
            alumnos.append(alumno)
            break
        except:
            print("Formato de entrada invalido.")        

def buscarPorNombre():
    apellido = input("Ingrese el apellido a buscar: ")
    for alu in alumnos:
        if alu["apellido"] == apellido:
            for x,y in alu.items():
                    print(x,": ",y)
        
    
def buscarPorSexo():
    m,f = 0,0
    for alu in alumnos:
        if alu.get("sexo").upper() == "M":
            m+=1
        elif alu.get("sexo").upper() == "F":
            f+=1
    print("Varones: ",m,"\nMujeres: ",f)
    
def buscarPorEdad():
    cont1, cont2 = 0,0
    edad = int(input("Ingrese la edad: "))    
    for alu in alumnos:
        if alu["edad"] <= edad:
            cont1+=1
        else:
            cont2+=1
    print("Hay ",cont1," alumnos hasta ",edad," años.")
    print("Hay ",cont2," alumnos mayor de ",edad," años.")
    
    