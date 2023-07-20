import requests

# Actualmente el plan gratuito de esta API son 250 request por mes
API_URL = 'http://api.weatherstack.com/current'

# La key se encuentra como comentario en la entrega 1 de este desafio
API_KEY = ''

# Diccionario vacío para almacenar los datos de cada ciudad
city_data = {}

# Obtener la temperatura actual en una ubicación específica utilizando una API de clima
def get_current_temperature(city):
    try:
        params = {
            'access_key': API_KEY,
            'query': city
        }
        # Realizar la solicitud GET a la API con los parámetros especificados
        api_result = requests.get(API_URL, params)
        
        # Verificar si la solicitud fue exitosa (código de respuesta 200)
        if api_result.status_code == 200:
            # Convertir la respuesta JSON en un diccionario de Python automáticamente
            api_response = api_result.json()
            
            # Verificar si los datos esperados están presentes en la respuesta
            if 'location' in api_response and 'current' in api_response:
                location = api_response['location']['name']
                temperature = api_response['current']['temperature']

                # Agregar el api_response al diccionario utilizando la ciudad como clave
                city_data[city] = api_response

                # Aqui estan almacenadas todos los datos separados por ciudad consultada
                # print(city_data)
                
                # Devolver los valores
                return location, temperature
            
            else:
                print("Datos faltantes en la respuesta de la API")
        else:
            print("Error en la solicitud a la API:", api_result.status_code)
    
    # Capturar posibles errores
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud a la API:", e)
