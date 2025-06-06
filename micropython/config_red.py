import network
import time
from machine import Pin

def conectar_wifi(lista_redes):
    wlan = network.WLAN(network.STA_IF) #se crea una instancia con el adaptador fisico
    wlan.active(True)
    
    # Desconectar la red si es que está conectada.
    if wlan.isconnected():
        wlan.disconnect()
        
    for red in lista_redes:
        #prin("\nIntentando conectar a: {red['ssid']}...")
        wlan.connect(red['ssid'], red['password'])
        
        timeout = 0
        while not wlan.isconnected() and timeout < 10:
            
            mostrar_buscar_con_rasp = Pin("LED", Pin.OUT)
            mostrar_buscar_con_rasp.value(1)
            
            print(".", end = "")
            time.sleep(1)
            timeout += 1
        
        if wlan.isconnected():
            mostrar_buscar_con_rasp.value(0)
            
            print("\n✅ Conectado a:", red['ssid'])
            return True
        else:
            print(f"\n❌ No se pudo conectar a: {red['ssid']}")
    
    
tiempo_rojo = 0.5
tiempo_amarillo = 0
tiempo_verde = 0.7
        