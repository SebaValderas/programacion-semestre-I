#While
edad=15
num= 0


#Bucle infinito, *tener cuidado con esto*
''' while edad<18:
        print("Eres menoir de edad")
'''

#Bucle infinito
'''while True:
        print(num)
        num +=2
'''

#bucle 1
num = 0
while num <= 0:
    print(num)
    num+=2
#este bucle hace que el numnero inicial, que es 0, se sume de 2 en 2 hasta llegar a 100
    
#bucle 2, usa while y else
num = 0
while num <= 200:
    print(num)
    num+=2
else:
    ("Bucle terminado")

#Bucle 3, usa while e if
while num <= 300:
    print(num)
    num += 2
    if num == 250:  #Mover if izquierda
        print("Mi condicion es igual a 250")

#Uso de break
while num <= 400:
    print(num)
    num += 2
    if num == 350:  #mover if izquierda
        print(Fore.MAGENTA + "Se detiene la ejecución")
        break
print(num)
print("Bucle terminado")

#Usao del continue
print('Impresión de numeros de 0 al 50 (Incrementando de 1 en 1) + continue if == 40')
num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)

#un loop infinito junto a un break
"""while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)"""  

#For
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

#Creando lista con un for
for i in range(1,11):
    print(i)

