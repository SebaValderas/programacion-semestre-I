#Datos numericos
edad = 18 #entero
estatura= 1.79 #real
peso= 95.5 #real
complejo = 1+ 6j #complejo

print('Mido {estatura} y mi peso es de {peso}')
print('Impresiónde numeros complejos, ',complejo, "\n")

#Transformación real a entero
print('Trasnformación', int(peso))

#Transformando entero a real
print('Transformación' ,float(edad))

#Operaciones

imc = peso / (estatura**2) #peso por altura al cuadrado
print(f"Imc= {imc}\n")


''' format es una manera de elegir el formato de lo que queremos imprimir
{:,2f}.format para decimales. La f representa un flotante'''

# DATOS DE CADENAS DE CARACTERES
asignatura = 'PROGRAMACIÓN'
carrera = 'Ingeniería Civil en Informatica'
print("La asignatura de ",asignatura,  " corresponde a la carrera de ",carrera)

#LEN cuenta la cantidad de caracteres, puede servir cuando trabajemos con parrafos

print('La cantidad de caracteres de la palabra ', asignatura, 'es de:',len(asignatura)) 

# VALORES BOOLEANOS
ampolleta = False
interruptor = True

#Podemos transformar cualquier valor a un Booleano (al igual que un string, int, etc)
print(bool(0))
print(bool(""))
print(bool([]))  
print(bool("False"))
print(bool(1)) 
print("\n")

# INICIALIZAR LISTAS
nueva_lista = list()
otra_lista = []
print('esta es una nueva lista vacia', nueva_lista)
print('Esta es otra lista vacía', otra_lista)

#Creando Listas
lista_equipos = ["Colocolo", "Arsenal", "Barcelona", "Real Madrid"]
lista_mixta = ["Messi" , "35 años", "Argentina"]
print(lista_mixta)

#Buscando elementos en lista
print(lista_equipos[0]) #elemento numero 1
print(lista_equipos[1]) #elemento numero 2
#print(lista_equipos[6]) #incorrecto
print("Posicion -2 de la lista mixta:",lista_mixta[-2]) #impresión desde atras hacia adelante

#Cambiando un elemnto de una lista
#Reasignando el valor de la 3° posicion de la lista
lista_equipos[3] = "Manchester United"

#Sacando los elementos de una lista y le damos variables
data_asig = [10023,"Programación",1,True]
cod,ramo,semestre,estado = data_asig
print(ramo)

# Tuplas (no mutables)
newtupla = (tuple)
grupo1 = ("Chile", "Argentina", "perú", "1200")
print(type(grupo1))

#Buscando el primer elemento de una tupla
print(grupo1[0])

#Consultando cuantas veces se repite un elemento en una tupla
print("El elemento se repite: ",grupo1.count("Chile"))

#Consultando la posición de un elemento en una tupla
print("Indice del elemento:",grupo1.index ("Chile"))

#Reasignando el primer elemento de una lista
grupo1[0] = "Constanza"
print(grupo1)

#Consultando un fragmento de tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

# SETS (conjuntos) - estructuram fija
#formas de inicializar un set
conjunto_vacio = set()
print(type(conjunto_vacio))
conjunto_colores = set({"Azul", "amarillo", "verde", "morado", "gris"})#utilizando función set
conjunto_animales = {"gato", "perro", "loro"} #utilizando llaves
print(f'el primer set contiene  los siguientes colores: ', conjunto_colores)
print('segundo set contiene los siguientes animales: ', conjunto_animales)
conjunto_animales.add("Celeste")
print('el set de colores lo conforman', conjunto_colores)

#Diccionarios
diccionario1 = dict()
diccionario2 = {}
datos_personales= {
    "Nombre": "Seba",
    "Carrera": "Ingeniería en Informática",
    "Edad": "18"
    }
print("Diccionario inicial:",datos_personales)

#Consultando cantidad de elementos en un diccionario
print(len(datos_personales))

#accediendo a un elemnto de un diccionario
print(datos_personales["Carrera"])

#Actualizar un elemento
datos_personales["Nombre"]= "Sebastián"
print("Diccionario nuevo: ", datos_personales)

#Agregando un nuevo clave 
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario nuevo:",datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario nuevo:",datos_personales)

hospital = {
    "nombre" : "Hospital San Jose",
    "direccion" : "Dr. Guillermo Buhler 1765",
    "ciudad" : "Osorno"
}