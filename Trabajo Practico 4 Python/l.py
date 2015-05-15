'''
Created on 4/5/2015

@author: leonardo
'''
def calcularArea(lado):
    return (lado*lado)

while True:
    try:
        lado = int(input("Ingrese un lado del cuadrado: "))    
        break    
    except:
        print("Error: Formato invalido.")

print("La suerficie del cuadrado es: ",calcularArea(lado))