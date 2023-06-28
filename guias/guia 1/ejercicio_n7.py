
print("Ingrese el número al que desea encontrar su factorial:")
num = int(input())

fact2 = 1

if num == 0:
    fact1 = 1
    print("El factorial de su número es:", fact1)
else:
    for i in range(1, num+1):
        fact2*=i
    print("El factorial de su número es:", fact2)





