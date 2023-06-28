#EJERCICIO N°1 
def ingresar_numeros():
    ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))
    lista = []

    for i in range(ingresar):
        numero = int(input("> "))               #PARES E IMPARES INVERTIDOS
        lista.append(numero)

    return lista


def sum_numeros(lista):
    sumatoria = sum(lista)

    return sumatoria


def pares_impares(lista):
    par = []
    impar = []

    for numero in lista:
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    return par, impar

lista = ingresar_numeros()
print("Los números ingresados son:", lista)

sum_total = sum_numeros(lista)
print("La sumatoria de los números ingresados es:", sum_total)

par, impar = pares_impares(lista)
sum_pares = sum_numeros(par)
sum_impares = sum_numeros(impar)

print("La sumatoria de los números pares ingresados es:", sum_pares)
print("La sumatoria de los números impares ingresados es:", sum_impares)