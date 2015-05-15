'''
Created on 5/5/2015

@author: leonardo
'''
from pyparsing import nums

def sumarDigitos(numStr):
    suma = 0
    for i in range(len(numStr)):
        suma += int(numStr[i:(i+1)])
    return suma

while True:
        try:
            num = str(input('Ingese un numero entero: '))
            break

        except:
            print('Error: Formato de entrada invalido.')
            
print("La suma de sus digitos es: ",sumarDigitos(num))