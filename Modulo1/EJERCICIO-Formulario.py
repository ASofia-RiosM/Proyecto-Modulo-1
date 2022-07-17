nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
correo = input("Introduce tu correo electrónico: ")
telefono = input("Introduce tu teléfono: ") #No se transforma a int porque puede iniciar en 0 y fallaría

print("Nombre: " + nombre)
print("Apellido: "+ apellido)
print("Edad: %s años" %(edad))
print("Correo: " + correo)
print("Teléfono: " + telefono)