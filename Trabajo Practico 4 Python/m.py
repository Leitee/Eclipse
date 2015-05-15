'''
Created on 4/5/2015

@author: leonardo
'''

def calcularRango():
    if((x <= l2) & (x >= l1)):
        print("El numero ingresado esta dentro del rango.")
    else:
        if(x > l2):
            print("El numero ingresado esta a la derecha del rango.")
        elif(x < l1):
            print("El numero ingresado esta a la izquierda del rango.")

while True:
    try:
        l1 = 10
        l2 = 50
        x = int(input('Ingrese un numero entero a buscar: '))
        break

    except:
        print('Error: Formato de entrada invalido')

calcularRango()
        