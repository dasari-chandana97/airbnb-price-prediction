function login(){

    let username = document.getElementById("username").value;

    let password = document.getElementById("password").value;


    if(username=="" || password==""){

        document.getElementById("message").innerHTML =
        "Please enter username and password";

    }

    else{

        document.getElementById("message").innerHTML =
        "Login Successful ✅";


        setTimeout(function(){

            window.location.href="/dashboard";

        },1000);

    }

}