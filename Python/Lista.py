"""
El problema trata de calcuclar el precio del envio por cada servicio. 
El precio por envio normal es de $100
El precio por envio rapido es $150
A ese precio base se le agrega un porcentaje por peso
hasta 5kg +5% de 5kg hasta 20kg +10% y mayor a 20kg un +20%
Tmb hay que tener en cuenta el porcentaje segun la zona de envio
Z1 norte +5%, Z2 centro +10% y Z3 sur +15%
"""

print('Bienvenido a Pandora Envios \n\nCalcule su envio:')

op = 's'
while(op == 's'):  
    while True:
        try:
            zona = int(input('ingrese la zona de envio 1=(Z1) 2=(Z2) 3=(Z3): '))
            peso = float(input('ingrese el peso del paquete: '))
            prioridad = input('ingrese tipo de prioridad (normal) (rapida): ')
            break

        except:
            print('Error: Formato de entrada invalido')        

    def calcularPrecioZona():
        if(zona == 1):
            return 1.05
        elif(zona == 2):
            return 1.10
        elif(zona == 3):
            return 1.15
                
    def calcularPrecioPeso():
        if(peso <= 5):
            return 1.05
        elif((peso > 5) & (peso <=20)):
            return 1.10
        elif(peso > 20):
            return 1.20    
    
    def calcularCosto():
        if(prioridad == 'normal'):
            return 100  * calcularPrecioZona() * calcularPrecioPeso()
        elif(prioridad == 'rapida'):
            return 150 * calcularPrecioZona() * calcularPrecioPeso()
    
    print('Su envio cuesta ', calcularCosto())
    op = input('Desea calcular otro envio? (s/n): ')


