'''
Created on 5/5/2015

@author: leonardo
'''

def compararString(num, tex):
    if(len(tex) == num):
        return True
    else:
        return False
    
while True:
    try:
        tex = str(input("Ingrese el texto a comparar: "))
        num = int(input("Ingrese un numero a comparar: "))
        break
    except:
        print("Error de formato de entrada.")
                
print("Tienen longitud",("distinta","igual")[compararString(num, tex)])