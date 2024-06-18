# https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_08_10/?format=TSV&compressed=true

import urllib.request
from urllib.error import URLError

def pib(url):
    pais = input('dime las iniciales de un país: ')
    try:
        with urllib.request.urlopen(url) as response:
            # Leer el contenido del archivo y decodificarlo
            data = response.read().decode('utf-8')
            # Dividir el contenido en palabras y contar las palabras
            lineas = data.split()
            encabezado = lineas[0].strip().split('\t')
            return encabezado
    except urllib.error.URLError as e:
        return f"Error al acceder al archivo en {url}: {e}"

# Ejemplo de uso
url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_08_10/?format=TSV"
pib_pais = pib(url)
print(pib_pais)