'''Escribe un programa que recoja un texto y escriba cada letra del texto en una
línea distinta.'''
texto = input("Escriba un texto:")
for c in range(0, len(texto),1):
    print(texto[c])