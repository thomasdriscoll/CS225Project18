$(document).ready(function(){
  $('.menu_bar_item').mouseenter(function() {
    $(this).css({
      backgroundColor: 'Blue'
    });
  }).mouseleave(function(){
    $(this).css({
      color: 'LightSkyBlue',
      backgroundColor: 'DarkBlue'
    })
  });
});
