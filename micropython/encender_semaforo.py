import luces_semaforo
import config_red
import enviar_datos
import recibir_modo_led

def cargar_semaforo():
    
    ledRojo = 15
    ledAmar = 14
    ledVerde = 13
    
    a = 0
    while True:
        datos = enviar_datos.recibir_datos_fb()
        
        
        
        if datos.get("modo") == "manual" and datos.get("color") == "rojo":
            a +=1
            
            print("DETENER ROJO")
            luces_semaforo.apagar(ledVerde, ledAmar)
            luces_semaforo.lz_roja(ledRojo)
            
            
        elif datos.get("modo") == "manual" and datos.get("color") == "amarillo":
            print("DETENER AMARILLO")
            luces_semaforo.apagar(ledRojo, ledVerde)
            luces_semaforo.luz_amarillo(ledAmar, config_red.tiempo_rojo)
            
            
        elif datos.get("modo") == "manual" and datos.get("color") == "verde":
            print("DETENER VERDE")
            luces_semaforo.apagar(ledRojo, ledAmar)
            luces_semaforo.lz_verde(ledVerde)
            continue
        
        
        elif datos.get("modo") == "automatico" and datos.get("color") == "ciclo":
            luces_semaforo.luz_roja(ledRojo, config_red.tiempo_rojo)
            luces_semaforo.luz_amarillo(ledAmar, config_red.tiempo_rojo)
            luces_semaforo.luz_verde(ledVerde, config_red.tiempo_rojo)