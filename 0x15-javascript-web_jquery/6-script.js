$(function () {
  const clickDiv = $('#update_header');

  clickDiv.bind('click', function () {
    $('header').text('New Header!!!');
  });
});
