from datetime import datetime
'''7. Escribe un programa que recoja la hora del día y devuelva un saludo, según
las siguientes reglas:
INTERVALO DE horaS SALUDO
[7,12) Buenos días
[12, 20) Buenas tardes
En otro caso Buenas noches'''

fecha = datetime.now()
hora = int(fecha.strftime("%H"))
match hora:
    case hora if hora >=7 and hora <12:
         print("BUENOS DIAS")
    case hora if hora >=12 and hora <20:
        print("BUENAS TARDES")
    case hora if hora>=20:
        print("BUENAS NOCHES")
