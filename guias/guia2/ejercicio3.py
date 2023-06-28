#EJERCICIO N°3
#BISIESTO: CADA 4 AÑOS -- MULTIPLO DE 100 NO -- MULTIPLO DE 400 SI
def bisiesto() :
    
    from time import sleep
    años = list(range(0, 2024))

    for i in años:

        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            sleep(1/2)
            print(f"#####{i} es bisiesto#####")
            
        else:
            print(f"{i} no es bisiesto")

bisiesto()

