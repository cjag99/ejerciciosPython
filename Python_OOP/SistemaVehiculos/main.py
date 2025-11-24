from Coche import Coche
from Moto import Moto
from Camion import Camion


def main():
    distancia = 200

    # Coche
    try:
        coche = Coche("Seat Ibiza", 2020)
        consumo_coche = coche.calcular_consumo(distancia)
    except Exception as e:
        consumo_coche = f"Error al calcular consumo del coche: {e}"

    # Moto
    try:
        moto = Moto("Yamaha MT-07", 2019)
        consumo_moto = moto.calcular_consumo(distancia)
    except Exception as e:
        consumo_moto = f"Error al calcular consumo de la moto: {e}"

    # Camión
    try:
        camion = Camion("Volvo FH", 2018)
        # El método de Camion puede requerir un parámetro adicional 'carga'.
        try:
            consumo_camion = camion.calcular_consumo(distancia, 2)  # ejemplo: carga=2 toneladas
        except TypeError as e1:
            consumo_camion = f"Error al calcular consumo del camión: {e1}"
    except Exception as e2:
        consumo_camion = f"Error al calcular consumo del camión: {e2}"

    print(f"Consumo para {distancia} km:")
    try:
        print(f"- Coche ({coche.modelo}): {consumo_coche}L")
    except NameError:
        print(f"- Coche: {consumo_coche}")
    try:
        print(f"- Moto  ({moto.modelo}): {consumo_moto}L")
    except NameError:
        print(f"- Moto: {consumo_moto}")
    try:
        print(f"- Camión ({camion.modelo}): {consumo_camion}L")
    except NameError:
        print(f"- Camión: {consumo_camion}")


if __name__ == "__main__":
    main()
