// VIEW CAROUSEL //
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 4000,
  wrap: true
})

const spinnerLink = document.getElementById("spinner-link").addEventListener('click', changeClass);

function changeClass(e) {
  
    const spinner = document.querySelector("#spinner");
    spinner.classList.toggle("d-none");
}

$(function() {
    $('#flash-messages').delay(500).fadeIn('normal', function() {
       $(this).delay(2500).fadeOut();
    });
 });

 function goBack() {
    window.history.back();
    }





    