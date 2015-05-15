'''
Created on 5/5/2015

@author: leonardo
'''
from datetime import *

def edades():
    return 0
    
while True:
    try:
        ahora = datetime.now()
        edad1 = input("Ingrese la primer edad: ")
        edad2 = input("Ingrese la segundo edad: ")
        break
    except:
        print("Error: Formato invalido.")
        
a = strptime(edad1[:10], "%Y-%m-%d")      
        
print(ahora.date())   