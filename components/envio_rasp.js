async function enviar(btn1, btn2, btn3) {
    
    try {
        
        const response = await fetch('https://semaforo-cd648-default-rtdb.firebaseio.com/',{
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                boton1: btn1,
                boton2: btn2,
                boton3: btn3
            })
        }
    );

    const data = await response.json();
    return data;

    } catch (error) {
        console.log("Erro al enviar datos");
    }

}