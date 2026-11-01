
import math

import requests
from tabulate import tabulate


URL_API = "https://dolarapi.com/v1/dolares"


def solicitar_monto() -> float:
    """Solicita un monto positivo en pesos argentinos."""
    while True:
        try:
            entrada = input("Ingresá un monto en ARS: ")
            monto = float(entrada)

            if not math.isfinite(monto):
                print("Error: ingresá un número finito.")
                continue

            if monto <= 0:
                print("Error: el monto debe ser mayor a cero.")
                continue

            return monto

        except ValueError:
            print("Error: ingresá un número válido.")


def obtener_cotizaciones() -> list[dict]:
    """Consulta DolarAPI y obtiene las cotizaciones oficial y blue."""
    try:
        respuesta = requests.get(URL_API, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()

        if not isinstance(datos, list):
            raise ValueError("La API no devolvió una lista.")

        cotizaciones = [
            dolar
            for dolar in datos
            if isinstance(dolar, dict)
            and dolar.get("casa") in ("oficial", "blue")
        ]

        casas = {dolar["casa"] for dolar in cotizaciones}

        if casas != {"oficial", "blue"} or len(cotizaciones) != 2:
            raise ValueError("Faltan cotizaciones del dólar.")

        return cotizaciones

    except requests.exceptions.RequestException as error:
        print(f"Error de conexión con DolarAPI: {error}")
        return []

    except (ValueError, TypeError) as error:
        print(f"Error en los datos de DolarAPI: {error}")
        return []


def convertir_a_dolares(
    monto_ars: float,
    precio_venta: float
) -> float:
    """Calcula cuántos dólares se compran con un monto en pesos."""
    if not math.isfinite(precio_venta) or precio_venta <= 0:
        raise ValueError("El precio de venta debe ser válido y positivo.")

    return monto_ars / precio_venta


def mostrar_tabla(
    monto_ars: float,
    cotizaciones: list[dict]
) -> None:
    """Muestra las cotizaciones y los importes convertidos."""
    filas = []

    for dolar in cotizaciones:
        nombre = dolar["nombre"]
        compra = float(dolar["compra"])
        venta = float(dolar["venta"])

        if not math.isfinite(compra) or compra < 0:
            raise ValueError("El precio de compra no es válido.")

        total_usd = convertir_a_dolares(monto_ars, venta)

        filas.append([
            nombre,
            f"${compra:,.2f}",
            f"${venta:,.2f}",
            f"USD {total_usd:,.2f}"
        ])

    encabezados = [
        "Dólar",
        "Compra",
        "Venta",
        "Total convertido"
    ]

    print()
    print(tabulate(
        filas,
        headers=encabezados,
        tablefmt="grid"
    ))


def main() -> None:
    """Ejecuta el programa principal del conversor de divisas."""
    print("=== CONVERSOR DE DIVISAS ===")

    monto_ars = solicitar_monto()
    print(f"Monto ingresado: ${monto_ars:,.2f} ARS")

    print("\nConsultando cotizaciones...")
    cotizaciones = obtener_cotizaciones()

    if not cotizaciones:
        print("No fue posible obtener las cotizaciones.")
        return

    try:
        mostrar_tabla(monto_ars, cotizaciones)

    except (ValueError, TypeError, KeyError) as error:
        print(f"Error al procesar las cotizaciones: {error}")

    except OverflowError as error:
        print(f"Error numérico durante la conversión: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
