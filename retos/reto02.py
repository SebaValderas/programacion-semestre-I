nombre= input(f'Ingrese el nombre del estudiante: ')
nombre= input(f'Ingrese el nombre del alumno: ')
asignatura= input(f'Ingrese la asignatura: ')
lab1=float(input(f'Ingrese nota de laboratorio número 1: '))
lab2= float(input(f'ingrese nota laboratorio número 2:'))
promedio= lab1*0.3+lab2*0.7

datos_alumnos= {"Nombre del almuno:": nombre,
 "Asignatura: ":asignatura,
"Nota laboratorio 1: ":lab1,
"Nota laboratorio 2: ":lab2,
"Promedio laboratorio: ":promedio}


print(datos_alumnos)




