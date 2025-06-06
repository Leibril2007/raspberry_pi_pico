from config_red import conectar_wifi
import config_red
import enviar_datos
import dht11
import encender_semaforo


REDES = [
    # nombre de la red, su contraseña
    #{'ssid': 'rockemma', 'password': 'rm123456'},
    {'ssid': 'POCO X3 Pro', 'password': 'Shaday88'},
    {'ssid': 'SA,GP.', 'password': '12345678'},
    {'ssid': 'TIGO-26D3-5G', 'password': 'Elohim3110#'},
    {'ssid': 'E-Learning-SCL-2025', 'password': 'Educ@cion.2024'},
    
]

if conectar_wifi(REDES):
    print("Conectado a Wifi - Ejecutando programa principal")
    
    dht11.programa_dht11()
    encender_semaforo.cargar_semaforo()   
    
else:
    print("Modo offline - Funcionalidades limitadas")
