'''
Created on 7/5/2015

@author: leonardo
'''
numeros = []

for i in range(5):
    while True:
        try:
            numeros.append(int(input("Ingrese los numeros de la lista: ")))         
            break
        except:
            print("Error de fomato invalido.")

copia = [i**2 for i in numeros]

print("La lista origina es: ",numeros)
print("La lista nueva es: ",copia)