pro = str(input("Ingresa el Nombre del Producto"))
t = float(input("Ingresa el total de tu compra"))
nom = str(input("Ingresa el Tu Nombre"))
tf = 0
if t > 100:
    descuento = t * 0.10
    tf = t - descuento
    
    print(f" Felicidades ",nom," Tienes un descuento del 10% en el producto ",pro," y el total a pagar es de ",tf)
    
else: print(f" El total a pagar es de ",tf)