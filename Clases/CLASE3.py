numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
operador = input("Ingrese un operador (+, -, *, /): ")

if operador == "+":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Operador no válido.")


