'''6. Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal), teniendo en cuenta que:
a. Nota menor de 5 es suspenso.
b. Nota entre 5 y 6 (sin llegar) es suficiente.
c. Nota entre 6 y 7 (sin llegar) es bien.
d. Nota entre 7 y 9 (sin llegar) es notable.
e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
f. Nota igual a 10 es matrícula de honor.
g. Cualquier otro valor numérico fuera de este rango es un error.'''
notaFinal = float(input("Introduce tu calificación numérica y diré tu nota final:"))
match notaFinal:
    case notaFinal if notaFinal < 5:
        print("SUSPENSO")
    case notaFinal if notaFinal >= 5 and notaFinal < 6:
        print("SUFICIENTE")
    case notaFinal if notaFinal >= 6 and notaFinal < 7:
        print("BIEN")
    case notaFinal if notaFinal >= 7 and notaFinal < 9:
        print("NOTABLE")
    case notaFinal if notaFinal >= 9 and notaFinal < 10:
        print("SOBRESALIENTE")
    case 10.0:
        print("MATRÏCULA DE HONOR")
    case notaFinal if notaFinal < 0 or notaFinal > 10:
        print("NOTA NO VÁLIDA")