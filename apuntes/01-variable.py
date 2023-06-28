# comentario de una línea
''' Comentario 
Multilinea'''
nombre = 'seba'

#Imprimir texto y una variable
print("hola soy",nombre)

#Imprimiendo una variable
print(nombre)

# Variable tipo numerico
edad = 18

#Imprimiendo texyo y una variable numerica
print("Hola, soy Seba y tengo ",edad)

#Imprimiendo 2 variables en una misma linea
print("Hola mi nombre es", nombre, "y tnego", edad)

#Actualizando variables(Mutabilidad)
nombre = "Pedro"
name = "Juan"
print ("Hola mi nuevo nombre es", nombre)
print ("Hola mi nuevo nombre es", name)

#Variables en una sola linea (No es recomendable)
ciudad, region, pais, year = "Osorno", "Los Lagos", "Chile", 2004.
print("Yo naci en la ciudad de", ciudad,", region de",region,pais,", el año",int(year))

#Input
nombre1 = input("¿Cuál es tu nombre?\n")
edad1 = input("¿Cual es tu edad?\n")
print("Tu nombre es:",nombre1,"y tu edad es", edad1)