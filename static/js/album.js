
// IIFE - Immediately Invoked Function Expression
(function(yourcode) {

    // The global jQuery object is passed as a parameter
    yourcode(window.jQuery, window, document);

  }(function($, window, document) {

    // The $ is now locally scoped 

   // Listen for the jQuery ready event on the document
   $(function() {

    //Getting albums
    var albumer
    // Getting images in album

    var $bilder = $('.bilder');
    // Writing images to html
    
    // Album updates on click


    // Change picture
    var $hoyre = $('#hoyre');
    var $venstre = $('#venstre');

    $hoyre.click(function(){
      let $alBilder =$('.alBilde');
      let index = $alBilder.index($clickedImg);
      if (index === $alBilder.length - 1){
        $modalImg.attr('src', $alBilder[0].src);
        $caption.text($alBilder[0].alt);
        $clickedImg = $alBilder[0]
      }
      else{
        $modalImg.attr('src', $alBilder[index + 1].src);
        $caption.text($alBilder[index + 1].alt);
        $clickedImg = $alBilder[index + 1]
      }

    });
    $venstre.click(function(){
      let $alBilder =$('.alBilde');
      let index = $alBilder.index($clickedImg);
      let len = $alBilder.length - 1;
      if (index === 0){
        $modalImg.attr('src', $alBilder[len].src);
        $caption.text($alBilder[len].alt);
        $clickedImg = $alBilder[len]
      }
      else{
        $modalImg.attr('src', $alBilder[index - 1].src);
        $caption.text($alBilder[index - 1].alt);
        $clickedImg = $alBilder[index - 1]
      }

    });



    // Open the modal
    var $modal = $('.modal1');
    var $navbar = $('.navbar');
    var $modalImg = $('#img01');
    var $caption = $('#caption-tekst');
    var $clickedImg;

     // Åpner modal når den blir klikket
    $bilder.delegate('.alBilde','click',function(){
        $clickedImg = $(this)[0];
        $modal.css('display', 'block');
        $navbar.css('display', 'none');
        $modalImg.attr('src', $clickedImg.src);
        $caption.text($clickedImg.alt);
    });
    // Lukker modal
    var $span = $('.closer')
    $span.click(function(){
      $modal.css('display', 'none')
      $navbar.css('display', 'block');
    });

    //DOM code


   });


   // annen kode
  
}));
