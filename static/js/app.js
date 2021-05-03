// VIEW CAROUSEL //
const myCarousel = document.querySelector('#myCarousel')
const carousel = new bootstrap.Carousel(myCarousel, {
  interval: 4000,
  wrap: true
})

// $(function(){
//     // You used .myCarousel here. 
//     // That's the class selector not the id selector,
//     // which is #myCarousel
//     $('#myCarousel').carousel();
//   });

// SPINNER //
const spinnerLink = document.getElementById("spinner-link").addEventListener('click', changeClass);

function changeClass(e) {
  
    const spinner = document.querySelector("#spinner");
    spinner.classList.toggle("d-none");
}

// FLASH MESSAGES //
$(function() {
    $('#flash-messages').delay(500).fadeIn('normal', function() {
       $(this).delay(2500).fadeOut();
    });
 });

 // BACK BUTTON //
function goBack() {
    window.history.back();
}

// FORWARD BUTTON //
function goForward(){
    window.history.go(1);
}


function showWelcomeMessage() {

}






    