
import datetime
import random
fol = random.randint(100,1000)
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pro = str(input("Ingresa el Nombre del Producto "))
t = float(input("Ingresa el total de tu compra "))
nom = str(input("Ingresa el Tu Nombre "))
tien = str(input("Ingresa el Nombre de la Tienda "))

descuento = 0
tf = t
if t > 100:
    descuento = t * 0.10
    tf = t - descuento
    print(" -------------------------------- TIKET DE LA TIENDA --------------------------------------")
    print(f"Tienda : ",tien)
    print(f"Folio : ",fol)
    print(f"Fecha y Hora : ",fecha)
    print(" ------------------------------------------------------------------------------------------")
    print(f"Cliente : ",nom)
    print(f"Producto : ",pro)
    print(f"Total de la Cuenta : ",t)
    print(f"Descuento Aplicado : ",descuento)
    print(f"Total a Pagar : ",tf)
    
    
else:  
    print(" ---------------------------------------------- TIKET DE LA TIENDA ---------------------------------------------------------")
    print(f"Tienda : ",tien)
    print(f"Folio : ",fol)
    print(f"Fecha y Hora : ",fecha)
    print(" ---------------------------------------------------------------------------------------------------------------------------")
    print(f"Cliente : ",nom)
    print(f"Producto : ",pro)
    print(f"Total de la Cuenta : ",t)
    print(f"Descuento Aplicado : ",descuento)
    print(f"Total a Pagar : ",tf)