'''
Created on 7/5/2015

@author: leonardo
'''

nros = [i for i in range(11)]

def eliminarValor(nros, nro):
    nros.remove(nro)
    return nros

while True:
    try:
        n = int(input("Ingrese el numero a eliminar de la lista: "))         
        break
    except:
        print("Error de fomato invalido.")
            

print("La lista origina es: ",nros)
print("La lista nueva es: ",eliminarValor(nros, n))