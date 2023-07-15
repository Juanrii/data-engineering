-- Las siguientes consultas fueron aplicadas en Amazon Redshift mediante el cliente dBeaver

-- Creacion de tabla para la entrega 1. API de clima
CREATE TABLE clima_ciudades (
  ciudad VARCHAR(100),
  pais VARCHAR(100),
  region VARCHAR(100),
  latitud FLOAT,
  longitud FLOAT,
  zona_horaria VARCHAR(100),
  hora_local TIMESTAMP,
  temperatura FLOAT,
  codigo_clima INTEGER,
  iconos_clima VARCHAR(500),
  descripciones_clima VARCHAR(500),
  velocidad_viento FLOAT,
  grado_viento INTEGER,
  direccion_viento VARCHAR(10),
  presion INTEGER,
  precipitacion FLOAT,
  humedad INTEGER,
  cobertura_nubes INTEGER,
  sensacion_termica FLOAT,
  indice_uv INTEGER,
  visibilidad FLOAT,
  es_de_dia BOOLEAN
);

-- Obtener todas las columnas
SELECT * FROM clima_ciudades;