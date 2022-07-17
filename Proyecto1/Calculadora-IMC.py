#Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura, 
# desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).
#Obtener los datos
try:
    nombre = input("Introduzca su nombre: ")
    apellido_paterno = input("Introduzca su apellido paterno: ")
    apellido_materno = input("Introduzca su apellido materno: ")
    edad = int(input("Introduzca su edad: "))
    peso = float(input("Introduzca su peso en kilogramos: "))
    estatura = float(input("Introduzca su estatura en metros: "))
except:
    print("Datos incorrectos. Para la edad, peso y estatura, ingrese datos numéricos")
    exit()

#Calcular el IMC
IMC = peso / (estatura**2)

#Desplegar los datos en pantalla
print("Nombre: %s" %(nombre,))
print("Apellido paterno: %s" %(apellido_paterno,))
print("Apellido materno: %s" %(apellido_materno,))
print("Edad: %s años" %(edad))
print("Peso: %s" %(peso))
print("Estatura: %s" %(estatura))
print("Su Índice de Masa Corporal (IMC) es: %s" %(IMC))
