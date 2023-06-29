### LABORATORIO 4, EJERCICIO 2###

a = ["Rojo, ", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]


def palabra_larga(a):
    palabra_mas_larga = ""

    for palabra in a:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


def encontrar_corta(b):
    palabra_mas_corta = b  # Suponemos que la primera palabra es la más corta inicialmente

    for palabra in b:
        if len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra

    return palabra_mas_corta


def concatenar_listas(a, b):
    c = a + b
    return c


def mayusculas(c):
    lista_mayusculas = [elemento.upper() for elemento in c]
    return c


def lista_alfabateca(c):
    c = sorted(c)
    return c
