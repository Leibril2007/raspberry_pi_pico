import { cargarTempHum } from "./temperatura_humedad.js";

async function recibir_datos_th(){

    try {
        const response = await fetch("https://semaforo-cd648-default-rtdb.firebaseio.com/dht11.json");
        const data = await response.json();
        console.log(data);

        let dataHum = data.hum;
        let dataTemp = data.temp;
    
        cargarTempHum(dataHum, dataTemp);

        return data;

    } catch (error) {
        console.log("Error al recibir datos", error);
    }

}

export { recibir_datos_th }