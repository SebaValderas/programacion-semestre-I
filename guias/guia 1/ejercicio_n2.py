# EJERCICIO 2
'''
2. Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 

'''
s1 = 500
s2 = 456
sum1 = 500
sum2 = 456

while s1 < 801:
    s1 += 10
    sum1 += s1
    s2 -= 10
    sum2 += s2

c = sum1+sum2-s2
print(c)
