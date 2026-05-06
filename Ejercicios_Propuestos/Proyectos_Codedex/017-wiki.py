# =========================================================
# PROYECTO: Consumir la API de Wikipedia con Python
# =========================================================
#
# OBJETIVO:
# Obtener y mostrar un resumen de Wikipedia usando una API.
#
# TECNOLOGÍAS UTILIZADAS:
# - Python
# - requests
# - API REST de Wikipedia
#
# =========================================================
# ERROR ENCONTRADO DURANTE EL DESARROLLO
# =========================================================
#
# Inicialmente se intentó usar:
#
#   respuesta.json()
#
# pero aparecía el siguiente error:
#
# requests.exceptions.JSONDecodeError:
# Expecting value: line 1 column 1 (char 0)
#
# ---------------------------------------------------------
# ¿QUÉ SIGNIFICA ESTE ERROR?
# ---------------------------------------------------------
#
# Python intentó convertir la respuesta del servidor
# a formato JSON, pero la respuesta estaba vacía
# o no era un JSON válido.
#
# =========================================================
# CAUSA REAL DEL PROBLEMA
# =========================================================
#
# Al inspeccionar la respuesta del servidor:
#
#   print(respuesta.status_code)
#   print(respuesta.text)
#
# se descubrió el verdadero error:
#
#   403 Forbidden
#
# Wikipedia estaba bloqueando la petición porque
# no se estaba enviando un "User-Agent".
#
# =========================================================
# ¿QUÉ ES UN USER-AGENT?
# =========================================================
#
# Es un encabezado HTTP (header) que identifica
# qué aplicación está realizando la petición.
#
# Muchos servidores y APIs bloquean peticiones
# que parecen bots o scripts desconocidos.
#
# =========================================================
# SOLUCIÓN
# =========================================================
#
# Se agregó un header llamado "User-Agent"
# simulando una aplicación válida:
#
# headers = {
#     "User-Agent": "MiProyectoPython/1.0"
# }
#
# Después de eso, Wikipedia permitió el acceso
# y devolvió correctamente el JSON.
#
# =========================================================
# CÓDIGO FINAL FUNCIONAL
# =========================================================

import requests

# URL de la API de Wikipedia en español
url = (
    "https://es.wikipedia.org/api/rest_v1/page/summary/"
    "Python_(lenguaje_de_programación)"
)

# Headers HTTP
# Se utiliza User-Agent para identificar la aplicación
headers = {
    "User-Agent": "MiProyectoPython/1.0"
}

# Realizar petición GET al servidor
respuesta = requests.get(url, headers=headers)

# Verificar que la petición fue exitosa
if respuesta.status_code == 200:

    # Convertir respuesta JSON a diccionario Python
    datos = respuesta.json()

    # Mostrar resumen del artículo
    print(datos["extract"])

else:
    # Mostrar código de error en caso de fallo
    print(f'Error: {respuesta.status_code}')


# =========================================================
# CONCEPTOS APRENDIDOS
# =========================================================
#
# ✅ APIs REST
# ✅ Peticiones HTTP
# ✅ Método GET
# ✅ JSON
# ✅ Headers
# ✅ User-Agent
# ✅ Manejo de errores
# ✅ Status codes HTTP
# ✅ Consumo de servicios externos
#
# =========================================================