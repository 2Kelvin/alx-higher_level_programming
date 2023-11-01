$(function () {
  const redDiv = $('#toggle_header');
  const header = $('header');
  redDiv.bind('click', function () {
    if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    } else {
      header.removeClass('red');
      header.addClass('green');
    }
  });
});
