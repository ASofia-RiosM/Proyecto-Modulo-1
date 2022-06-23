nombre = input("¿Cómo te llamas?")
print("Hola " + nombre)

edad= input("¿Cúantos años tienes?")
print(type(edad))
print(f"{nombre} tiene {edad} años") 

#Programa que pide dos números al usuario y los suma
numero_uno= int(input("Introduce un número, por favor: "))
numero_dos= int(input("Introduce otro número, por favor: "))
numero_tres = numero_uno + numero_dos

print(f"El resultado de la suma es {numero_tres}")