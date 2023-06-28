nombre_curso = "Ultimate Python"
descripcion_curso = """"
Ultimate Python
Este curso contiene todo el material necesario para poder
aprender a programar en Pyhton XD
"""
print(nombre_curso, descripcion_curso)
# len es para saber cuantos caracteres hay en el string
print(len(nombre_curso))
print(nombre_curso[0])
'''Aquí es para acceder a un caracter en especifico del string'''
print(nombre_curso[0:8])
'''esta parte funciona para "recortar" una porción del string
ya que [0:8] indican desde que caracter hasta cual caracter desea seleccionar
en este caso es la palabra "Ultimate" pq es desde el 0 hasta el 8'''
print(nombre_curso[9:]
      )  # al no tener numero despues de : se lee hasta el final
# funciona de la misma forma al revés
# si no colocamos nada en [:] se leerá completo
