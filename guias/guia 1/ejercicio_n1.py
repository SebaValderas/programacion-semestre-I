
#Ejercicio n°1
#Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente parrafo: 

parrafo="""La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica."""

eliminar=".,\n"
for caracter in eliminar:
    parrafo=parrafo.replace(caracter, "")

parrafo=parrafo.lower()
var_1=parrafo.count("universidad")
var_2=parrafo.split()
tupla=tuple(var_2)

print(tupla)
print("En el parrafo la palabra universidad se repite", var_1, "veces.")

