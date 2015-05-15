'''
Created on 5/5/2015

@author: leonardo
'''

def compararNumeros(n1, n2, n3):
    if ( (n1==(n2+n3)) | ((n1+n2)==n3) | ((n1+n3)==n2) ):
        return "La suma de 2 de ells es igual al tercero."
    else:
        return "La condicion no se cumple."
        
while True:
        try:
            n1 = int(input('Ingrese el primer numero: '))
            n2 = int(input('Ingrese el segundo numero: '))
            n3 = int(input('Ingrese el tercer numero: '))
            break

        except:
            print('Error: Formato de entrada invalido') 
            
print(compararNumeros(n1, n2, n3))        