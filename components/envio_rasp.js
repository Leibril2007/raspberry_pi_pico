async function enviar(modoEnv, colorEnv) {
    
    try {
        
        const response = await fetch('https://semaforo-cd648-default-rtdb.firebaseio.com/estado.json',{
            method: 'PATCH',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                modo: modoEnv,
                color: colorEnv,
            })
        }
    );

    const data = await response.json();
    console.log("DATOS ENVIADOS :D");
    return data;

    } catch (error) {
        console.log("Erro al enviar datos");
    }

}

export { enviar };