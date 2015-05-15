'''
Created on 7/5/2015

@author: leonardo
'''
numeros = []

def sustituirNegativos(nros):
    for i in range(len(nros)):
        if(nros[i] < 0 ):
            nros[i]= 0
    return nros    

for i in range(5):
    while True:
        try:
            numeros.append(int(input("Ingrese el numero  a cargar en la lista: ")))         
            break
        except:
            print("Error de fomato invalido.")
            

print("La lista origina es: ",numeros)
print("La lista nueva es: ",sustituirNegativos(numeros))