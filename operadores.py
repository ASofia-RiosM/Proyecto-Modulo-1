# operadores aritméticos
print(2 + 2) #suma
print(4 - 2) #resta
print(3 * 7) #multiplicación
print(15 / 2) #división
print(11 % 4) # % <- módulo (11 módulo 4) RESIDUOS DE DIVISIÓN 
print(11 // 4) # // <- división de piso (11 división de piso 4) PARTE ENTERA DE UNA DIVISIÓN
print (2**3) # ** <- potencia ELEVAR UN NÚMERO A UNA POTENCIA

# operadores en cadenas 
print("Hola" + "mundo") #concatenación
print("Hola" * 3) #repetición
print("Hola" + "mundo" *3) #concatenación y repetición
# MEJORAS
print("Hola" + " mundo")
print("Hola " * 3)
print(("Hola " + "mundo ") *3)

# operadoes de comparación (SON DE TIPO BOOL)
print("Hola" == "hola") # igual que
print("Hola"!= "hola") # distinto que
print(3 < 11) # menor que
print(3 > 11) # mayor que
print(11 >= 10) # mayor o igual que
print(10 <= 11) # menor o igual que

# operadores de existencia
print("ola" in "hola") # De existecia
print("ola" not in "hola") # De inexistencia

# operadores booleanos
print(True or False) # "or" Verifica que se cumpla una condición
print(True and False) # "and" Verifica que se cumplan las dos condiciones

# operadoes de asignación
x = 1 # operador de asignación estándar
x += 2 # operador de asignación suma
x *= 3 # operador de asignación multiplicación
x %= 4 # operador de asignación módulo
print(x)