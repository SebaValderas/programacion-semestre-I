print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado=input("Ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break
        op = input("ingrese operación: ")
        if op.lower() == "salir":
            break
        
    

        