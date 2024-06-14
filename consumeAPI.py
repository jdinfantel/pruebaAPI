import requests

# URL de la API
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Realizar una solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON a un diccionario de Python
    data = response.json()
    # Imprimir el contenido del JSON
    print(data)
else:
    print(f'Error en la solicitud: {response.status_code}')
