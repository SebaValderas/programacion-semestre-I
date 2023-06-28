#EJERCICIO N°5
num = int(input("Ingrese los numeros que desee > "))
numeros = list()

while num < 0 :
    num = int(input("Ingrese un entero positivo > "))
else :

    print("Para cerrar el ciclo, ingrese el (-1)")

    numeros.append(num)

while num != -1 :

    if num < 0 :

        num = int(input("Ingrese un entero positivo > "))

    else :

        num = int(input("> "))
        numeros.append(num)

enteros_pos = [i for i in numeros if i >= 0]


print("Numeros ingresados exitosamente")

num_mayor = max(enteros_pos)                            
print(f"El mayor numero ingresado es {num_mayor}")

num_suma = sum(enteros_pos)
print(f"La suma de los numeros ingresados es {num_suma}")

num_impares = [i for i in enteros_pos if (i % 2) != 0]
sum_impares= sum(num_impares)
print(f"La suma de los numeros impares ingresados es {sum_impares}")

promedio = (num_suma / len(numeros))                                    
print(f"El promedio de los numeros ingresados es {promedio}")           

if num_mayor > promedio :
    print(f"{num_mayor} es mayor que el promedio.")
else :
    print(f"{num_mayor} es menor que el promedio")