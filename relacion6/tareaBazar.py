import funciones
ventas = {"Arroz":{"L": 250, "M": 300, "X": 275, "J": 400, "V": 350},
          "Manzanas":{"L": 180, "M": 220, "X": 200, "J": 260, "V": 310},
          "Brocoli":{"L": 320, "M": 290, "X": 310, "J": 370, "V": 400},
          "Leche":{"L": 150, "M": 180, "X": 210, "J": 230, "V": 190}}

#Funcion que ejecuta el programa
def main():
    global ventas
    ventasMensuales = funciones.getVentasMensuales(ventas)
    productoMasVendido = funciones.getMaxVentasMensuales(ventasMensuales)
    #Construimos las cadenas a usar porque no se puede concatenar str con elementos del dict
    strProductoMasVendido = ""  
    strProductoMenosVendido = ""
    keyProductoMasVendido = ""
    for key in productoMasVendido:
        strProductoMasVendido += str(key) + "-> " + str(productoMasVendido[key])
        keyProductoMasVendido = str(key)
    productoMenosVendido = funciones.getMinVentasMensuales(ventasMensuales)
    for key in productoMenosVendido:
        strProductoMenosVendido += str(key) + "-> " + str(productoMenosVendido[key])
    funciones.menuBazar()
    while True:
        opcion = funciones.seleccionarOpcionBazar()
        match opcion:
            case 1:
                funciones.mostrarVentasMensuales(ventasMensuales)
            case 2:
                print("El producto más vendido es: " + strProductoMasVendido)
                print("El producto menos vendido es: " + strProductoMenosVendido)
            case 3:
                funciones.mostrarVentasProductoMax(keyProductoMasVendido, ventas)
            case 4:
                funciones.mostrarDiaMaxVentasPorProducto(ventas)
            case 5:
                print("Finalizando programa...")
                break
        input("Pulse cualquier tecla para continuar...")

main()