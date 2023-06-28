n1 = input("Ingresa el primer número")
n2 = input("Ingresa el segundo número")
n1 = int(n1)
n2 = int(n2)

suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1/n2

mensaje = f"""
Resultados operaciones entre {n1} y {n2}
Suma: {suma}
Resta: {resta}
Multiplicación: {multi}
División: {div} 
"""
print(mensaje)
