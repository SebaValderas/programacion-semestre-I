#Ejercicio n°4
#Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por Nicomaco de Gerasa

x= int(input("Ingrese el numero deseas: "))
impar=(x*(x-1)) + 1
y= 0

for i in range(x):
    y = y + impar
    if i == (x-1):
        break
    impar = impar + 2 
    print(impar, end="-")
    
print("El cubo de", x, "es:", y)