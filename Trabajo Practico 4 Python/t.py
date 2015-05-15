'''
Created on 5/5/2015

@author: leonardo
'''

monedas = [100, 50, 20, 10, 5, 2, 1]

def calcularCambio(monto, monedas):
    copyMoneda = [0 for i in monedas]
    for i in range(len(monedas)):
        while monedas[i] <= monto:            
            copyMoneda[i]+=1
            monto -= monedas[i]        
    return copyMoneda

while True:
    try:
        monto = float(input("Ingrese el monto a cambiar: "))
        break
    except:
        print("Error formato invalido.")

for i in range(len(calcularCambio(monto, monedas))):
    print("$",monedas[i], "= ", calcularCambio(monto, monedas)[i], " unidad(es).")