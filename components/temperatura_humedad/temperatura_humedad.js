function cargarTempHum(){

    let div = document.createElement('div');
    div.className = "temp-hum-base";

    let h1 = document.createElement('h2');
    h1.className = "tit-temp";
    h1.textContent = "Temperatura:";
    div.appendChild(h1);


    let tempValor = document.createElement('h2');
    tempValor.className = "temp-valor";
    tempValor.textContent = "h";
    div.appendChild(tempValor);

    let humedad = document.createElement('h2');
    humedad.className = "tit-hum";
    humedad.textContent = "Humedad:";
    div.appendChild(humedad);


    let humValor = document.createElement('h2');
    humValor.className = "hum-valor";
    humValor.textContent = "t";
    div.appendChild(humValor);


    let imgVent = document.createElement('img');
    imgVent.src = "https://github.com/Leibril2007/img_App/blob/main/ventilador.png?raw=true";
    div.appendChild(imgVent);


    document.body.appendChild(div);

}



export { cargarTempHum }


window.onload = cargarTempHum();