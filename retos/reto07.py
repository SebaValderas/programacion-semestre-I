def longitud_palabras():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()
    dic_palabras = {palabra: len(palabra) for palabra in palabras}
    print(dic_palabras)


longitud_palabras()
