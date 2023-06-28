animal = "chanchito feliz"
print(animal.upper())  # esto es para colocarlo el string en mayuscula
print(animal.lower())  # esto coloca el string en minuscula
print(animal.capitalize())  # coloca la primera letra del string en mayuscula
# esto coloca en mayuscula las primeras letras de todas las palabras
print(animal.title())
# borra los espacios inutiles que están en los extremos del string
print(animal.strip())
print(animal.lstrip())  # es para sacar los espacios de la izquierda
print(animal.rstrip())  # es para sacar los espacios de la derecha
# se puede juntar estos metodos, por ejemplo:
# aquí borra los espacios inutiles y coloca todo mayuscula
print(animal.strip().capitalize())

# aquí busca una cadena de texto en especifico y especifica el indice
print(animal.find("feliz"))
# reemplaza una porción de texto
print(animal.replace("chanchito", "vaquita"))
# busca si hay ciertos caracteres y lo representa como boolean
print("vaquita" in animal)
# lo mismo pero revisa si no está, también es boolean
print("vaquita" not in animal)
