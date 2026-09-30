function predictPrice(){


let data={

    location:
    document.getElementById("location").value,


    room_type:
    document.getElementById("room_type").value,


    minimum_nights:
    document.getElementById("minimum_nights").value,


    reviews:
    document.getElementById("reviews").value,


    availability:
    document.getElementById("availability").value

};



fetch("/predict",{

    method:"POST",

    headers:{
        "Content-Type":"application/json"
    },


    body:JSON.stringify(data)

})


.then(response=>response.json())


.then(result=>{


document.getElementById("result").innerHTML =

"Estimated Price : $" + result.predicted_price;


})


.catch(error=>{

console.log(error);

});


}




// -------- Chart Code --------


const ctx = document.getElementById('priceChart');


if(ctx){

new Chart(ctx, {

type:'bar',

data:{

labels:[
"Manhattan",
"Brooklyn",
"Queens",
"Bronx"
],


datasets:[{

label:"Average Price",

data:[
250,
180,
140,
100
]

}]

}

});

}