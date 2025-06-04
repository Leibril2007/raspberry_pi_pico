import { buttonRed, buttonYellow, buttonGreen, buttonReinicio } from "../funcionalidad_botones/botones.js";

function createHeader() {
  
  const header = document.createElement('header');
  header.className = 'header';

  
  const logo = document.createElement('div');
  logo.className = 'logo';
  logo.textContent = '👑'; 


  const gameTitle = document.createElement('h1');
  gameTitle.className = 'game-title';
  gameTitle.textContent = 'Raspberry Pi Pico';

  
  const buttonsDiv = document.createElement('div');
  buttonsDiv.className = 'buttons';

  
  const buttonInicio = document.createElement('button');
  buttonInicio.textContent = 'Rojo';
  buttonInicio.onclick = () => buttonRed();

  const buttonOpciones = document.createElement('button');
  buttonOpciones.textContent = 'Amarillo';
  buttonOpciones.onclick = () => buttonYellow();

  const buttonSalir = document.createElement('button');
  buttonSalir.textContent = 'Verde';
  buttonSalir.onclick = () => buttonGreen();

  const buttonReset = document.createElement('button');
  buttonReset.textContent = 'Restaurar';
  buttonReset.onclick = () => buttonReinicio();


  
  buttonsDiv.appendChild(buttonInicio);
  buttonsDiv.appendChild(buttonOpciones);
  buttonsDiv.appendChild(buttonSalir);
  buttonsDiv.appendChild(buttonReset);

  
  header.appendChild(logo);
  header.appendChild(gameTitle);
  header.appendChild(buttonsDiv);


  document.body.appendChild(header);
}

window.onload = createHeader();

  