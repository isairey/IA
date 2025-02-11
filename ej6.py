import random
n = random.randint(1,10)
n1 = int(input("Adivina el Numero de 1 a 10 "))
print(f"\n El Numero Aleatorio es ",{n})
if n1 == n: print("Correcto has Adivinado el numero")
else: print("Es Incorecto")