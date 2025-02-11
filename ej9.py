t = float(input("Ingresa el total de tu compra"))
tf = 0
if t > 100:
    descuento = t * 0.10
    tf = t - descuento
    
    print(f"Tienes un descuento del 10% y el total a pagar es de ",{tf})
    
else: print(f" El total a pagar es de ",{tf})