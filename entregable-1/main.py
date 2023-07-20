# Importo el modulo weather_api
import weather_api

# Definir la funcion principal main
def main():
    # Agregue por el momento solo estas porque algunas no estan incluidas
    CITIES = [
        'Buenos Aires',
        'Cordoba',
        'Santa Fe',
        'Corrientes',
        'Entre Rios'
    ]
    
    # Tuve que realizar este bucle porque no hay otra forma de consultar
    # multiples ciudades al menos que se pague la subscripcion.
    # Por lo tanto cada iteracion costara 1 request
    for city in CITIES:
        # Obtener la temperatura actual en la ubicación especificada
        temperature_data = weather_api.get_current_temperature(city)
        # Mostrar la temperatura en caso de obtener los valores deseados
        if temperature_data:
            location, temperature = temperature_data
            print(u'Current temperature in %s is %d℃' % (location, temperature))

if __name__ == "__main__":
    main()
