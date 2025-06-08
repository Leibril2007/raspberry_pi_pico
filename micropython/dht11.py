import machine
import dht
import urequests
import ujson
import time
import luces_semaforo
import enviar_datos
import encender_semaforo
from encender_semaforo import ledRojo

def enviar_datos_tempHum(temp, hum):
    try:
        url = 'https://semaforo-cd648-default-rtdb.firebaseio.com/dht11.json'
        
        datos = {
            "hum": hum,
            "temp": temp
        }

        headers = {"Content-Type": "application/json"}

        response = urequests.patch(url, data=ujson.dumps(datos), headers=headers)

        print("Datos enviados a Firebase:", datos)

        response.close()

    except Exception as e:
        print("Error al enviar datos a Firebase:", e)
 


def programa_dht11():
    # Configura el pin de datos del DHT11 
    sensor = dht.DHT11(machine.Pin(16))

    while True:
        try:
            sensor.measure() #Recupera los datos
            temp = sensor.temperature() # Almacena la temperatura
            hum = sensor.humidity() # Almacena la humedad
            enviar_datos_tempHum(temp, hum)
            
            datos = enviar_datos.recibir_datos_fb()
            
            modo = datos.get("modo")
            color = datos.get("color")
            
            encender_semaforo.verificar_luz_roja(modo, color)
            
            
            print("Temperatura: {}°C".format(temp)) # format coloca el dato de la temperatura entre las llaves, similar a fprint
            print("Humedad: {}%".format(hum))

        except OSError as e:
            print("Error al leer el sensor:", e)
        
        time.sleep(2)# 


