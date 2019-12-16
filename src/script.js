

// features.addEventListener('submit', function (e){
//     console.log(e)
// })


function displayResult(data){
    document.querySelector('#result').value = data['first']
    
}

const firstReq = new XMLHttpRequest();

document.forms["features"].addEventListener('submit', function(e){
    e.preventDefault()
    fields = {}
    const elements = document.forms["features"].elements;
    for (var i = 0; i < 7; i++) {
        fields[i]= elements[i].value
    }
    console.log(fields)
    console.log(JSON.stringify(fields))
    
    fetch('http://127.0.0.1:5000/predict',{
        method: 'POST',
        body: JSON.stringify(fields)
    }).then((data)=> data.json()).then((data) => displayResult(data))

    //Older way to get requests
    // firstReq.open('GET', 'http://127.0.0.1:5000/predict');
    // firstReq.send();
    }
    


)

firstReq.addEventListener('load', function() {
	console.log('IT WORKED!!!');
	const data = JSON.parse(this.responseText);
	for (let planet of data.results) {
		console.log(planet.name);
	}
});
