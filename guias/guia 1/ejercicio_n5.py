# EJERCICIO 5
'''Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una 
lista y luego pida buscar algun numero dentro de los almacenados. Ademas que muestre 
la cantidad de ocurrencias de ese numero buscado.
'''
from random import randint
lista = [randint(40, 350) for x in range(20)]
print(lista)

busqueda = int(input("Ingrese un numero entre el 40 y el 350: "))
if busqueda in lista:
    repes = lista.count(busqueda)
    print("El número se encuentra en la lista")
    print("Cantidad de repeticiones: ", repes)
else:
    print("No se encontró el número")
