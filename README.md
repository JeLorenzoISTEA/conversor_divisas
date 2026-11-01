# Conversor de Divisas - Python

## Descripción

Programa desarrollado en Python que permite convertir un monto dado en pesos argentinos (ARS) a dólares estadounidenses (USD), utilizando las cotizaciones del dólar oficial y dólar blue.

Las cotizaciones se obtienen en tiempo real mediante la API pública DolarAPI.

El programa utiliza el precio de venta de cada cotización para calcular la cantidad de dólares que pueden comprarse con el monto ingresado.

## Funcionalidades

- Solicitar un monto en pesos argentinos.
- Validar que el monto ingresado sea numérico y positivo.
- Consultar las cotizaciones actuales mediante una API.
- Obtener los valores de compra y venta del dólar oficial y blue.
- Calcular la conversión de ARS a USD.
- Mostrar los resultados en una tabla.
- Manejar errores de conexión y datos inválidos.

## Tecnologías utilizadas

- Python 3
- requests: consultas HTTP a la API.
- tabulate: presentación de resultados en tablas.

API utilizada: https://dolarapi.com/v1/dolares

## Instalación

**1. Descargar el proyecto**

Clonar el repositorio o descargarlo como ZIP.

**2. Crear el entorno virtual**

```powershell
python -m venv .venv
```

**3. Activar el entorno virtual en Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Instalar las dependencias**

```powershell
python -m pip install -r requirements.txt
```

## Ejecución

Ejecutar desde la terminal:

```powershell
python main.py
```

Ingresar el monto en pesos argentinos solicitado por el programa.

El sistema consultará las cotizaciones y mostrará los resultados en una tabla.

## Manejo de errores

El programa contempla:

- Montos no numéricos, negativos o iguales a cero.
- Problemas de conexión con la API.
- Errores HTTP.
- Respuestas inválidas o incompletas.
- Cotizaciones que no permiten realizar la conversión.

## Integrantes

- Lorenzo Jeremias
