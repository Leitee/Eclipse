'''
Created on 4/5/2015

@author: leonardo
'''

def calcularPulgadas(n):
    return (n*39.37)

def calcularPies(n):
    return (calcularPulgadas(n)/12)

while True:
        try:
            metro = float(input("Ingrese la una medida en metros: "))            
            break

        except:
            print('Error: Formato de entrada invalido')
            
print("El valor ", metro, " es igual a ",calcularPulgadas(metro), " pulgadas.")
print("El valor ", metro, " es igual a ",calcularPies(metro), " pies.")