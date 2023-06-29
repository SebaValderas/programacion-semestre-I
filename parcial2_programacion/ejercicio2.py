n1 = float(input("Ingrese nota numero 1: "))
n2 = float(input("Ingrese nota numero 2: "))
n3 = float(input("Ingrese nota numero 3: "))
n4 = float(input("Ingrese nota numero 4: "))
n5 = float(input("Ingrese nota numero 5: "))
n6 = float(input("Ingrese nota numero 6: "))
n7 = float(input("Ingrese nota numero 7: "))
n8 = float(input("Ingrese nota numero 8: "))
n9 = float(input("Ingrese nota numero 9: "))
n10 = float(input("Ingrese nota numero 10: "))
notas = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
if notas < 7.0 or notas>70.0:
    print("Ingrese notas validas, deben ser mayores a 0.99  y menores 7.01") 
promedio = notas/10
print("El promedio de las notas de la asignatura de Programación es:",promedio)

