licencia = False
edad = 19
automovil = False

''' Este extracto está mal
if licencia:
    print("puedo manejar, ya que tengop licencia")
else:
    print("no tengo licencia para conducir")
'''
#Utilizando el primer condicional IF
if licencia:
    print('Puedo conducir porque tengo licencia')
else:
    print('No tengo licencia para conducir')

# Utilizando el segundo condicional IF
if edad:
    print('Puedo conducir porque soy mayor de edad')
else:
    print('No puedo conducir soy menor de edad')
    
#Utilizando el tercer condicional IF
if edad >= 18:
    print('Puedo conducir porque soy mayor de edad')
else:
    print('No puedo conducir soy menor de edad')

#If, elif, else
if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print('Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print('No puedo conducir no tengo ni la edad, ni licencia ni automovil')