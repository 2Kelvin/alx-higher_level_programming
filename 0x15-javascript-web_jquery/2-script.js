$(function () {
  const redDiv = $('#red_header');
  redDiv.bind('click', function() {
    $('header').css('color', '#FF0000');
  });
});

