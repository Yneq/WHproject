function getData(){
    fetch(
        "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
    )
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        console.log(data)
    })

}