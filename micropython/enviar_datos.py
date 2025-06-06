import urequests
import ujson

def enviar_datos_fb(datoRojo, datoAmar, datoVerde):
    try:
        url = 'https://semaforo-cd648-default-rtdb.firebaseio.com/semaforo.json'
        
        datos = {
            "rojo": datoRojo,
            "amarillo": datoAmar,
            "verde": datoVerde
        }

        headers = {"Content-Type": "application/json"}

        # PATCH actualiza los campos sin reemplazar toda la ruta
        response = urequests.patch(url, data=ujson.dumps(datos), headers=headers)

        print("Datos enviados a Firebase:", datos)

        response.close()

    except Exception as e:
        print("Error al enviar datos a Firebase:", e)
        
        
def recibir_datos_fb():
    try:
        url = 'https://semaforo-cd648-default-rtdb.firebaseio.com/estado.json'
        
        response = urequests.get(url)
        datos = response.json()
        
        print("datos recibidos de fb", datos)
        
        response.close()
        return datos
    
    except Exception as e:
        print("error al RECIBIR datos fb", e)
