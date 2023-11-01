$(function () {
  const redDiv = $('#red_header');
  redDiv.bind('click', function() {
    $('header').addClass('red');
  });
});

