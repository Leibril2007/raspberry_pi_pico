import luces_semaforo
import config_red
import enviar_datos

ledRojo = 15
ledAmar = 14
ledVerde = 13



def verificar_luz_roja(modoRec, colorRec):
    if modoRec == "manual" and colorRec == "rojo":
        print("DETENER ROJO")
        luces_semaforo.apagar(ledVerde, ledAmar)
        luces_semaforo.luz_roja_estatico(ledRojo)
    else:
        luces_semaforo.apagarDHT(ledRojo)
        verificar_luz_amarillo(modoRec, colorRec)

def verificar_luz_amarillo(modoRec, colorRec):
    if modoRec == "manual" and colorRec == "amarillo":
        print("DETENER AMARILLO")
        luces_semaforo.apagar(ledRojo, ledVerde)
        luces_semaforo.luz_amarillo(ledAmar, config_red.tiempo_rojo)
    else:
        verificar_luz_verde(modoRec, colorRec)


def verificar_luz_verde(modoRec, colorRec):
    if modoRec == "manual" and colorRec == "verde":
        print("DETENER VERDE")
        luces_semaforo.apagar(ledRojo, ledAmar)
        luces_semaforo.luz_verde_estatico(ledVerde)
    else:
        ciclo_de_luces(modoRec, colorRec)


def ciclo_de_luces(modoRec, colorRec):
    if modoRec == "automatico" and colorRec == "ciclo":
        
        luces_semaforo.luz_roja(ledRojo, config_red.tiempo_led)
        luces_semaforo.luz_amarillo(ledAmar, config_red.tiempo_led)
        luces_semaforo.luz_verde(ledVerde, config_red.tiempo_led)
        


def cargar_semaforo():
    
    #a = 0
    while True:
        datos = enviar_datos.recibir_datos_fb()
        
        modo = datos.get("modo")
        color = datos.get("color")
        
        verificar_luz_roja(modo, color)
        
            
