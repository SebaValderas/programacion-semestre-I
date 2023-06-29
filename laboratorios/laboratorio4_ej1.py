### LABORATORIO 4, EJERCICIO 1###

pacientes = [["Pedro", 1.78], ["Constanza", 1.56], [
    "Amanda", 1.62], ["Dario", 1.89], ["Fernanda", 1.67]]


def estatura_menor(pacientes):
    estatura_menor = float('inf')
    for paciente in pacientes:
        estatura = paciente[1]
        if estatura < estatura_min:
            estatura_min = estatura
    return round(estatura_min, 1)


def paciente_nuevo(pacientes, nuevo_paciente):
    pacientes.append(nuevo_paciente)


nuevo_paciente = ["Ricardo", 1.71]
paciente_nuevo(pacientes, nuevo_paciente)
print("Lista nueva: ", pacientes)


def buscar_paciente(pacientes, nombre):
    for paciente in pacientes:
        if paciente[0] == nombre:
            return paciente
    return None


nombre = "Dario"
buscar_paciente(pacientes, nombre)
