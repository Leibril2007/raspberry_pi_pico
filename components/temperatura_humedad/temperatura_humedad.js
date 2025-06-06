import { recibir_datos_th } from "./recibir_datos_dht11.js";

function cargarTempHum(hum, temp){

    let div = document.createElement('div');
    div.className = "temp-hum-base";

    let h1 = document.createElement('h2');
    h1.className = "tit-temp";
    h1.textContent = "Temperatura:";
    div.appendChild(h1);


    let tempValor = document.createElement('h2');
    tempValor.className = "temp-valor";
    tempValor.textContent = temp;
    div.appendChild(tempValor);

    let humedad = document.createElement('h2');
    humedad.className = "tit-hum";
    humedad.textContent = "Humedad:";
    div.appendChild(humedad);


    let humValor = document.createElement('h2');
    humValor.className = "hum-valor";
    humValor.textContent = hum;
    div.appendChild(humValor);


    let imgVent = document.createElement('img');
    imgVent.src = "https://github.com/Leibril2007/img_App/blob/main/ventilador.png?raw=true";
    div.appendChild(imgVent);

    if (temp >= 30){
        imgVent.src = "https://mir-s3-cdn-cf.behance.net/project_modules/source/bafb3929035897.55decb26f207b.gif";
        div.appendChild(imgVent);
    }

    document.body.appendChild(div);

}

setInterval(recibir_datos_th, 200)


export { cargarTempHum }


window.onload = recibir_datos_th();