""" a=7 
b=2

x=a 
x+=b  
print("x+=", x) 


x=a 
x-=b
print("x-=", x)  


x=a; 
x*=b;  
print("x*=", x)  

x=a; 
x/=b;  
print("x/=", x)  """

""" numero1 = 5
numero2 = 6

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2



print(suma)
print(resta)
print(multiplicacion)
print(division)
 """


""" ------------------------------------------------------------ """

print("***CALCULADORA CLIMATICA***")

celsius = float(input("Ingrese los grados en C°: "))

farenheit= (celsius * 9 / 5) + 32

print ("Los grados en F", farenheit)




num1 = float(input("Ingrese un numero"))
num2 = float(input("Ingrese otro numero"))

print("Seleccione una opcion \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División")

opcion = int(input("Ingrese una opción: "))

if opcion == 1:
    print("La suma es: ", num1 + num2)
elif opcion == 2:
    print("La resta es: ", num1 - num2)
elif opcion == 3:
    print("La multiplicación es: ", num1 * num2)
elif opcion == 4:
    print("La división es: ", num1 / num2)
else:
    print("Opción inválida")
