'''
Created on 7/5/2015

@author: leonardo
'''

lista = list()

def cargarElementos(nro):
        lista.append(nro)
        
def mostrarCola():
    #lista.reverse()
    [print(i) for i in lista]
        
for i in range(5):
    while True:
        try: 
            cargarElementos(int(input("Ingrese el numero a eliminar de la lista: ")))       
            break
        except:
            print("Error de fomato invalido.")
        
print(mostrarCola())