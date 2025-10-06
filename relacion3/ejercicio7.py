'''Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto.'''
texto = input("Introduzca un texto:")
letra = input("Introduzca una letra:")
numCoincidencias = 0
if letra.__len__() > 1:
    print("Eso no es una letra")
else:
    for c in range(texto.__len__()):
        if(texto[c] == letra):
            numCoincidencias+=1
        print("Para el texto", texto, "y la letra", letra, "hay", numCoincidencias, "coincidencias")
