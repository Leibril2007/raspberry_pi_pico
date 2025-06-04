import { enviar } from "../envio_rasp.js";
import { actualizarLuces } from "../script.js";

const luces = document.querySelectorAll('.luz');

async function buttonRed() {

    let modo = "manual";
    let color = "rojo";

    let envDato = enviar(modo, color);

    return envDato;
}
  
async function buttonYellow() {
    let modo = "manual";
    let color = "amarillo";

    let envDato = enviar(modo, color);
    
    return envDato;
}

async function buttonGreen() {
    let modo = "manual";
    let color = "verde";

    let envDato = enviar(modo, color);

    return envDato;
}

async function buttonReinicio() {
    let modo = "automatico";
    let color = "ciclo";
    let envDato = enviar(modo, color);

    return envDato;
}
  
export { buttonRed, buttonGreen, buttonYellow, buttonReinicio }