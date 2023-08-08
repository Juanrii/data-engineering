# Importo el modulo weather_api
import weather_api
import pandas as pd
# Utilizo redshift_connector porque tuve problemas con psycopg2
import redshift_connector


# Actualizar datos mediante cuidad-fecha, evita registros duplicados
def update_data(cursor, nombre_tabla, row, ciudad, fecha):
    update_query = f"UPDATE {nombre_tabla} SET hora_local = %s, temperatura = %s, codigo_clima = %s, iconos_clima = %s, descripciones_clima = %s, velocidad_viento = %s, grado_viento = %s, direccion_viento = %s, presion = %s, precipitacion = %s, humedad = %s, cobertura_nubes = %s, sensacion_termica = %s, indice_uv = %s, visibilidad = %s, ciudad = %s, fecha = %s WHERE ciudad = '{ciudad}' AND fecha = '{fecha}'"
    cursor.execute(update_query, (
        row['hora_local'], row['temperatura'], row['codigo_clima'], row['iconos_clima'],
        row['descripciones_clima'], row['velocidad_viento'], row['grado_viento'], row['direccion_viento'],
        row['presion'], row['precipitacion'], row['humedad'], row['cobertura_nubes'],
        row['sensacion_termica'], row['indice_uv'], row['visibilidad'], ciudad, fecha
    ))

# Insertar nuevos registros
def insert_data(cursor, nombre_tabla_redshift, data):
    insert_query = f"INSERT INTO {nombre_tabla_redshift} (ciudad, pais, region, latitud, longitud, zona_horaria, hora_local, temperatura, codigo_clima, iconos_clima, descripciones_clima, velocidad_viento, grado_viento, direccion_viento, presion, precipitacion, humedad, cobertura_nubes, sensacion_termica, indice_uv, visibilidad, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # Insertar multiples registros masivos
    cursor.executemany(insert_query, data)

# Acumular data a registrar
def prepare_data(df):
    data = []
    for index, row in df.iterrows():
        # Añadir cada fila a la lista de datos a insertar
        data.append(tuple(row))
    # Retornar todas las filas acumuladas en un solo query masivo
    return data


# Definir la funcion principal main
def main():

    # Datos de conexion
    hostname = 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com'
    database = 'data-engineer-database'
    username = 'juanrios0495_coderhouse'
    pwd = 'fkeJ90t2Y6'
    port_id = '5439'

    # Se realiza la conexion
    conn = redshift_connector.connect(
        host=hostname,
        port=port_id,
        database=database,
        user=username,
        password=pwd
    )

    # Se crea un objeto cursor para ejectuar consultas
    cursor = conn.cursor()

    # Agregue por el momento solo estas porque algunas no estan incluidas
    CITIES = [
        'Buenos Aires',
        'Cordoba',
        'Santa Fe',
        'Corrientes',
        'Rosario'
    ]
    
    data_to_insert = []

    # Verifica si se ha realizado alguna actualizacion
    updated = False

    # Tuve que realizar este bucle porque no hay otra forma de consultar
    # multiples ciudades al menos que se pague la subscripcion.
    # Por lo tanto cada iteracion costara 1 request
    for city in CITIES:

        # Obtener los datos para luego insertarlos en Redshift
        raw_data = weather_api.get_data(city)

        # Guardar los datos en caso de obtener los valores deseados
        if raw_data:

            # Creacion del DataFrame utilizando pandas
            df = pd.DataFrame(raw_data)

            # Eliminar duplicados basados las columnas ciudad y fecha
            df = df.drop_duplicates(subset=['ciudad', 'fecha'])

            # Tabla deseada
            nombre_tabla_redshift = 'clima_ciudades'

            # Se itera por cada fila para extraer la ciudad y la fecha
            # La tabla contiene una clave primaria compuesta (ciudad-fecha)
            # Se creo una nueva columna fecha que solo contiene el formato date Y-mm-dd
            for index, row in df.iterrows():
                ciudad = row['ciudad']
                fecha = row['fecha']

                # Query para verificar si ya existe la cambinacion ciudad-fecha
                query = f"SELECT 1 FROM {nombre_tabla_redshift} WHERE ciudad = %s AND fecha = %s"
                cursor.execute(query, (ciudad, fecha))
                # Obtener solo uno
                result = cursor.fetchone()

                # Si ya existe la combinacion ciudad-fecha, actualiza los campos
                if result:
                    update_data(cursor, nombre_tabla_redshift, row, ciudad, fecha)
                    updated = True
                # De lo contrario, inserta un nuevo registro
                else:
                    data_to_insert.append(prepare_data(df))
    
    # Si se realizo alguna actualizacion, hacer el commit
    if updated:
        conn.commit()

    # Realizar una comprension de la lista data para obtener todas las filas como elementos individuales
    data = [row for sublist in data_to_insert for row in sublist]
    if data:
        # Insertar multiples registros masivamente
        insert_data(cursor, nombre_tabla_redshift, data)
        conn.commit()

if __name__ == "__main__":
    main()
