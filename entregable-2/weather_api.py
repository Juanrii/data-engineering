import requests
from datetime import datetime

# Actualmente el plan gratuito de esta API son 250 request por mes
API_URL = 'http://api.weatherstack.com/current'

API_KEY = '2c7f1f192a5961fb41d5e6a89df7bfdc'

# Diccionario vacío para almacenar los datos de cada ciudad
city_data = {}
data = {};

# Obtener la temperatura actual en una ubicación específica utilizando una API de clima
def get_data(city):
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

                ciudad              = api_response['location']['name']
                pais                = api_response['location']['country']
                region              = api_response['location']['region']
                latitud             = api_response['location']['lat']
                longitud            = api_response['location']['lon']
                zona_horaria        = api_response['location']['timezone_id']
                hora_local          = api_response['location']['localtime']
                temperatura         = api_response['current']['temperature']
                codigo_clima        = api_response['current']['weather_code']
                iconos_clima        = api_response['current']['weather_icons']
                descripciones_clima = api_response['current']['weather_descriptions']
                velocidad_viento    = api_response['current']['wind_speed']
                grado_viento        = api_response['current']['wind_degree']
                direccion_viento    = api_response['current']['wind_dir']
                presion             = api_response['current']['pressure']
                precipitacion       = api_response['current']['precip']
                humedad             = api_response['current']['humidity']
                cobertura_nubes     = api_response['current']['cloudcover']
                sensacion_termica   = api_response['current']['feelslike']
                indice_uv           = api_response['current']['uv_index']
                visibilidad         = api_response['current']['visibility']

                # Se agrego una columna fecha como fue solicitado en la primera entrega
                fecha = datetime.strptime(hora_local, "%Y-%m-%d %H:%M").date()
                
                # Crear un diccionario con todos los datos
                data = {
                    'ciudad':               ciudad,
                    'pais':                 pais,
                    'region':               region,
                    'latitud':              latitud,
                    'longitud':             longitud,
                    'zona_horaria':         zona_horaria,
                    'hora_local':           hora_local,
                    'temperatura':          temperatura,
                    'codigo_clima':         codigo_clima,
                    'iconos_clima':         iconos_clima,
                    'descripciones_clima':  descripciones_clima,
                    'velocidad_viento':     velocidad_viento,
                    'grado_viento':         grado_viento,
                    'direccion_viento':     direccion_viento,
                    'presion':              presion,
                    'precipitacion':        precipitacion,
                    'humedad':              humedad,
                    'cobertura_nubes':      cobertura_nubes,
                    'sensacion_termica':    sensacion_termica,
                    'indice_uv':            indice_uv,
                    'visibilidad':          visibilidad,
                    'fecha':                fecha
                }

                # Devolver el diccionario con los datos
                return data
            
            else:
                print("Datos faltantes en la respuesta de la API")
        else:
            print("Error en la solicitud a la API:", api_result.status_code)
    
    # Capturar posibles errores
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud a la API:", e)
