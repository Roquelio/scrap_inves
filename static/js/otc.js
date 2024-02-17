

function fetchData() {
    // Hacer la solicitud a la API
    fetch('https://api.investing.com/api/financialdata/table/list/2110?fieldmap=general.slim')
        .then(response => response.json())
        .then(data => {
            // Obtener el precio de la respuesta
            const price = data.data[0].data[1];

            // Insertar el precio en el elemento con id "inves"
            document.getElementById('inves').innerHTML = price;
        })
        .catch(error => console.error('Error fetching data:', error));
}
fetchData()