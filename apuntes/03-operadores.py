a = 10
b = 15
c = 8
d = 4

#Operaciones
print("Suma entre a + b:",a + b)
print("Resta entre a - b:",a - b)
print("Multiplicación entre a * b:",a * b)
print("División entre a / b:",a / b)
print("El módulo entre a y b:",a % b)
print("El cociente entre b / c:",b // c)
print("El resultado de b elevado a c:",b ** c,"\n")

#Variable tipo float
t= 5.39 #tiempo por segundos
g= 9.81 #aceleración por gravedad

#operaciones con flotantes
v = t*g

print("La velocidad del objeto en caida libre es de: {v} m/s")
print("La velocidad del objeto en caida libre es de: {:.2f}".format(v)) #1 manera de formatear decimales
print(f"La velocidad del objeto en caida libre es de: {v:.2f}")         #2 manera de formatear decimales con f-string
print("La velocidad del objeto en caida libre es de:","%.2f" % v)       #3 utilizando el formateador %f

#Variables complejas
c2 = complex(3, -5)
print("numero complejo:" ,c2)

#multiplicar strings
print("hola"*5)

#operadores de comparación
print(a == b) #igual a
print(a != b) #desigual a
print(a > b)  #mayor que
print(a < b)  #menor que
print(c >= d) #mayor o igual que
print(c <= d) #menor o igual que

#Operadores Lógicos

bencina = True
encendido = False
edad = 19

#if
if bencina and encendido:
    print("El vehiculo se mueve")
else:
    print("El vehiculo no se mueve")

#or
if bencina or encendido:
    print("El vehiculo se mueve")
else:
    print("El vehiculo no se mueve")

#not y and
if not bencina and encendido:
    print("El vehiculo se mueve")
else:
    print("El vehiculo no se mueve")

#not y or
if not bencina or encendido:
    print("el vehiculo se mueve")
else:
    print("El vehiculo no se mueve")

#not, and y or juntos
if not bencina or (encendido and edad >= 18):
    print("El vehiculo se mueve")
else:
    print("El vehiculo no se mueve")    