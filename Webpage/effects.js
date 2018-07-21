$(document).ready(function(){
  $('.nav-item').mouseenter(function() {    
    if($(this).hasClass('current')){
      $(this).css({
        'backgroundColor': 'Blue',
      });
    }
    else{
      $(this).css({
        'backgroundColor': 'Blue',
        'border-bottom': '5px solid blue'
      });
    }
  }).mouseleave(function(){
    if($(this).hasClass('current')){
      $(this).css({
        'backgroundColor': 'DarkBlue',
      });
    }
    else{
      $(this).css({
        'backgroundColor': 'DarkBlue',
        'border-bottom': '5px solid DarkBlue'
      });
    }

  });
});
// Try to cut this down to like 5 lines, this if-else nonsense hurts my sensibilities
