console.log("app.js");


// VIEW CAROUSEL //
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 4000,
  wrap: true
})

console.log(carousel);



// async function resquest_wger() {
//     await axios.get(`https://wger.de/api/v2/exerciseinfo/?language=2`)
//     .then(function (response) {
//         // handle success
//         console.log(response);
//       })
//       .catch(function (error) {
//         // handle error
//         console.log(error);
//       })
// }


// resquest_wger();



// LOGIN AND USER FORMS - TOGGLE && EXPAND ON NAV CLICK  //

// window.onload = function () {

//     const loginLink = document.getElementById("login-link").addEventListener('click', changeClass);
//     const registerLink = document.getElementById("register-link").addEventListener('click', changeClass);
//     const registerCarouselLink = document.getElementById("register-carousel-link").addEventListener('click', changeClass);
// }

// function showLogin(form1, form2) {
//     form1.classList.remove("d-none");
//     form1.classList.remove("col-md-6");
//     form1.classList.add("col-md-12");
//     form2.classList.toggle("d-none");
// }

// function showRegister(form1, form2) {
//     form2.classList.remove("d-none");
//     form2.classList.remove("col-md-6");
//     form2.classList.add("col-md-12");
//     form1.classList.toggle("d-none");
// }

// function changeClass(e) {
//     const target = e.target;
//     const form1 = document.querySelector("#login");
//     const form2 = document.querySelector("#register");
   
 
//     if (target.id === "login-link") {
//         showLogin(form1, form2);

//     }
//     else if (target.id === "register-link") {
//         showRegister(form1, form2);
//     }

//     else {
//         showRegister(form1, form2);
//     }
// }




    
    