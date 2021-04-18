console.log("app.js");


// VIEW CAROUSEL //
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 4000,
  wrap: true
})

console.log(carousel);