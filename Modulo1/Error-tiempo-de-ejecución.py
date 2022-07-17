#numHuevos=12
#print("Tengo" + numHuevos + "huevos.")
#Esto es un error, porque no se puede concatenar un str con un int

#Opción 1 (se hace un cast a la variable numHuevos)
numHuevos = 12
print("Tengo"+ str(numHuevos)+"huevos.")

#Opción 2 (se utiliza %s para avisar la existencia de una variable)
print("Tengo %s huevos." %(numHuevos))