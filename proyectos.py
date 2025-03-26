#PARQUE DIVERSIONES 

#VARIABLES
""" nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


#CONDICIONALES
if edad < 12:
    print(f"{nombre}, deberá pagar $500")
else:
    print(f"{nombre}, deberá pagar $800") """


# LIBRERIA
""" print("BIENVENIDO A LA LIBRERIA BDS") 

nombre = input("Ingrese su nombre: ")
precioTotal = int(input("Ingrese el precio final de su compra: "))

if precioTotal < 2000:
    print(f"{nombre}, el valor total de su compra es: ${precioTotal}")
else:
    precioDescuento = precioTotal*0.15
    print(f"{nombre},por superar los $2000 obtuvo un descuento del 15%. El valor total de su compra es: ${precioTotal}-{precioDescuento}") """

""" print("Gracias por su compra 📖")  """

#ESTACIONAMIENTO

""" print("Estacionamiento BDS")

usoEstacionameinto = int(input("Ingrese el tiempo de uso del estacionamiento: "))

dosHoras = 50
masHoras = 30


if usoEstacionameinto < 2:
    print(f"El valor a pagar es: ${dosHoras}*{usoEstacionameinto}")
else:
    print(f"El valor a pagar es: ${masHoras}*{usoEstacionameinto}")

print("GRACIAS POR USAR ESTACIONAMIENTO BDS")  """

#COMPRA SUPER
""" 
precioCompra = int(input("Ingrese el precio total de su compra: "))

if precioCompra < 5000:
    print("No recibiste el cupón de $500, debes superar los $5000")
else: 
    print("Recibiste el cupón de $500, felicitaciones!")  """

#ENVIO GRATIS

precioProducto = float(input("Ingrese el precio del producto: "))

if precioProducto < 1000:
    print(f"Deberás pagar ${precioProducto}, más un envio de $200 ")
else:
    print(f"Deberás pagar ${precioProducto} y el envio es gratis")
