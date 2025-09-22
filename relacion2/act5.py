'''5. Escribe un programa que calcule el precio de entrada a un museo a partir de
la edad del visitante, teniendo en cuenta que:
a. Menores de 5 años entran gratis.
b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
d. Jubilados entran gratis.'''
edad = int(input("Dime tu edad y te diré el precio de tu entrada:"))
match edad:
    case edad if edad < 5 or edad >= 65:
        print("Tu entrada es gratis")
    case edad if edad >= 5 and edad < 18:
        print("Tu entrada vale 3€")
    case edad if edad >= 18 and edad < 65:
        print("Tu entrada vale 6€")