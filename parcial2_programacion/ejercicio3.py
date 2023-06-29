grupo1 = [100, 250, 300, 1000]
grupo1= [150, 250, 500, 1000]
grupo2 = set()
grupo2 = set()
buscando = 100
buscando2 = 500
buscando3 = 700
if buscando in grupo1 and buscando in grupo2:
    print("El precio $100 está en ambos sets")
else:
    print("El precio 100 no está en ambos grupos")
if buscando2 in grupo1 or buscando2 in grupo2:
    print("El precio ",buscando2 " se encuentra en alguno de los grupos")
else: 
    print("El precio ",buscando2"no se encuentra ninguno de los grupos")
if buscando3 in grupo1 or buscando3 in grupo2:
    print("El precio ", buscando3 )    




    #100, 250, 300, 1000
    #150, 250, 500, 1000
    # print("El precio ",buscando2 " se encuentra en alguno de los grupos")