## ejercicio 74

import urllib.request
from urllib.error import URLError

def contar_palabras_en_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            # Leer el contenido del archivo y decodificarlo
            data = response.read().decode('utf-8')
            # Dividir el contenido en palabras y contar las palabras
            palabras = data.split()
            numero_palabras = len(palabras)
            return numero_palabras
    except urllib.error.URLError as e:
        return f"Error al acceder al archivo en {url}: {e}"

# Ejemplo de uso
url = "https://www.geeksforgeeks.org/print-the-content-of-a-txt-file-in-python/"
numero_palabras = contar_palabras_en_url(url)
print(f"El archivo en la URL '{url}' contiene {numero_palabras} palabras.")