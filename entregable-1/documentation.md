Esta documentación describe la estructura y el significado de cada campo devuelto por la API en formato JSON. 

{
     "Buenos Aires" {
          "request":{...},
          "location":{...},
          "current":{...}
     },
     "Cordoba" {
          "request":{...},
          "location":{...},
          "current":{...}
     },
     "Santa Fe" {
          "request":{...},
          "location":{...},
          "current":{...}
     },
     "Corrientes" {
          "request":{...},
          "location":{...},
          "current":{...}
     },
     "Entre Rios" {
          "request":{...},
          "location":{...},
          "current":{...}
     }
}

API Doc: https://weatherstack.com/documentation

# API_KEY: Se encuentra como comentario en la entrega 1 de este desafio.

Cuenta gratuita: 250 request por mes

Request (Solicitud):

- type (tipo): El tipo de solicitud realizada, en este caso "City" (ciudad).
- query (consulta): La consulta realizada, en este caso "Buenos Aires, Argentina".
- language (idioma): El idioma utilizado en la respuesta, en este caso "en" (inglés).
- unit (unidad): La unidad utilizada para las mediciones, en este caso "m" (metros).

Location (Ubicación):

- name (nombre): El nombre de la ubicación, en este caso "Buenos Aires".
- country (país): El país de la ubicación, en este caso "Argentina".
- region (región): La región de la ubicación, en este caso "Distrito Federal".
- lat (latitud): La latitud de la ubicación, en este caso "-34.588".
- lon (longitud): La longitud de la ubicación, en este caso "-58.673".
- timezone_id (identificador de zona horaria): El identificador de la zona horaria de la ubicación, en este caso "America/      Argentina/Buenos_Aires".
- localtime (hora local): La hora local en formato "YYYY-MM-DD HH:MM", en este caso "2023-07-15 13:53".
- localtime_epoch (hora local en formato epoch): La hora local en formato epoch, en este caso 1689429180.
- utc_offset (desplazamiento UTC): El desplazamiento de la zona horaria con respecto a UTC, en este caso "-3.0" horas.

Current (Actual):

- observation_time (hora de observación): La hora de la observación en formato "HH:MM AM/PM", en este caso "04:53 PM".
- temperature (temperatura): La temperatura actual en grados Celsius, en este caso 13.
- weather_code (código de clima): El código numérico que representa el estado del clima.
- weather_icons (íconos de clima): Una lista de URL que proporcionan los íconos asociados al clima actual.
- weather_descriptions (descripciones de clima): Una lista de descripciones del clima actual.
- wind_speed (velocidad del viento): La velocidad del viento en kilómetros por hora.
- wind_degree (grado del viento): El grado o dirección del viento.
- wind_dir (dirección del viento): La dirección del viento en forma de siglas.
- pressure (presión): La presión atmosférica en milibares.
- precip (precipitación): La cantidad de precipitación en milímetros.
- humidity (humedad): El porcentaje de humedad.
- cloudcover (cobertura de nubes): El porcentaje de cobertura de nubes.
- feelslike (sensación térmica): La sensación térmica en grados Celsius.
- uv_index (índice UV): El índice UV actual.
- visibility (visibilidad): La visibilidad en kilómetros.
- is_day (es de día): Indica si es de día o de noche, con los valores "yes" (sí) o "no" (no).