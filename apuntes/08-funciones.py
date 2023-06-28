#inicializando una funcion

def mi_primera_funcion():
    print("Esta es mi primera funcion")

mi_primera_funcion()    

#Declarando una funcion y utilizando listas

def concatenar(lista1, lista2):
    return lista1 + lista2

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

#concatenar()

print(concatenar(lista1, lista2))

def multiplicacion(num1, num2):
    return num1*num2

#multiplicacion()

print(multiplicacion(2,10))

#funcion suma y resta por teclado

def suma(a, b):
    return a + b

def resta(a, b):
    return a-b

a= input("ingrese el primer numero: ")
b= input("ingrese el segundo numero: ")

#llamando funcion suma
resultado = suma(a,b)
print("la suma es de: ", resultado)

#llamando funcion resta
resultado2= resta(a,b)
print("la resta es de: ",resultado2)