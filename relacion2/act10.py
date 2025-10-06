'''10.Escribe un programa que a partir de información de un donante determine si
puede donar sangre. Las condiciones para donar son:
a. No se debe donar en ayunas.
b. Edad: Comprendida entre los 18 y 65 años.
c. Peso: Superior a 50kg.
d. Tensión arterial: dentro de límites adecuados para la extracción.
i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
f. Valores de hemoglobina:
i. En hombres: superior a 13,5 gramos por litro
ii. En mujeres: superior a 12,5 gramos por litro.
g. Plaquetas: más de 150.000 cc
h. Proteínas totales: más de 6 gr/dl.'''
ayunas = bool(input("indique si está en ayunas(true/false):"))
edad = int(input("Indique su edad:"))
peso = float(input("Indique su peso:"))
tBaja = int(input("Indique su tensión diastólica:"))
tAlta = int(input("Indique su tensión sistólica:"))
pulso = int(input("Indique sus pulsaciones:"))
esHombre = bool(input("indique si es varón o mujer(true/false):"))
hemoglobina = float(input("Indique sus valores de hemoglobina:"))
plaquetas = float(input("Indique sus valores de plaquetas:"))
protTotales = int(input("Indique sus valores de proteinas totales:"))
if not ayunas:
    if edad >= 18 and edad <= 65:
        if peso > 50:
            if tBaja >= 50 and tBaja < 100:
                if tAlta>= 90 and tAlta <= 180:
                    if pulso >= 50 and pulso <= 110:
                        if plaquetas > 150:
                            if protTotales > 6:
                                if esHombre:
                                    if hemoglobina > 13.5:
                                        if plaquetas > 150:
                                            if protTotales > 6:
                                                print("PUEDE DONAR")
                                            else:
                                                print("NO PUEDE DONAR")
                                        else:
                                            print("NO PUEDE DONAR")        
                                    else:
                                       print("NO PUEDE DONAR")
                                else:
                                    if hemoglobina > 12.5:
                                       print("PUEDE DONAR")
                                    else:
                                       print("NO PUEDE DONAR")
                            else:
                               print("NO PUEDE DONAR")
                        else:
                            print("NO PUEDE DONAR")   
                    else:
                        print("NO PUEDE DONAR")
                else:
                   print("NO PUEDE DONAR")
            else:
               print("NO PUEDE DONAR")
        else:
            print("NO PUEDE DONAR")
    else:
       print("NO PUEDE DONAR") 
else:
    print("NO PUEDE DONAR")