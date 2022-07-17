#Calcular la superficie o área de un cuadrado

lado = int(input("Ingresa la medida del lado del cuadrado"))
superficie= lado * lado * lado #Esto es un error de lógica porque no es la fórmula correcta
print("La superficie del cuadrado es: " + str(superficie))

#Correcto
lado = int(input("Ingresa la medida del lado del cuadrado"))
superficie = lado * lado #Fórmula correcta, no va a haber error de lógica
print("La superficie del cuadrado es: " + str(superficie))
