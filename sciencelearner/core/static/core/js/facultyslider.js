$('.owl-carousel').owlCarousel({
  loop:true,
  margin:10,
  autoplay:true,
  nav:true,
  autoplayTimeout:2000,
  stagePadding:50,
  dots:false,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:3
      },
      1000:{
          items:5
      }
  }
})