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
def insert_data(cursor, nombre_tabla, df):
    insert_query = f"INSERT INTO {nombre_tabla} (ciudad, pais, region, latitud, longitud, zona_horaria, hora_local, temperatura, codigo_clima, iconos_clima, descripciones_clima, velocidad_viento, grado_viento, direccion_viento, presion, precipitacion, humedad, cobertura_nubes, sensacion_termica, indice_uv, visibilidad, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # Lista de valores a insertar
    data_values = [tuple(row) for row in df.values]
    # Insertar multiples registros
    cursor.executemany(insert_query, data_values)


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
    
    # Tuve que realizar este bucle porque no hay otra forma de consultar
    # multiples ciudades al menos que se pague la subscripcion.
    # Por lo tanto cada iteracion costara 1 request
    for city in CITIES:

        # Obtener los datos para luego insertarlos en Redshift
        data_to_insert = weather_api.get_data(city)

        # Guardar los datos en caso de obtener los valores deseados
        if data_to_insert:

            # Creacion del DataFrame utilizando pandas
            df = pd.DataFrame(data_to_insert)

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
                # De lo contrario, inserta un nuevo registro
                else:
                    insert_data(cursor, nombre_tabla_redshift, df)
            
            conn.commit()
            # Muestra por consola los datos ingresados en formato json
            print(data_to_insert)

if __name__ == "__main__":
    main()
