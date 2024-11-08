import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingrese que tan largo quiere su contraseña: "))
resultado=""
for i in range(longitud):
    resultado+=random.choice(caracteres)

print(f"Tu contraseña de longitud {longitud} es: {resultado}")    
