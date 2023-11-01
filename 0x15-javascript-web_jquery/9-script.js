$(document).ready(function () {
  const divHello = $('#hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data) {
    divHello.text(data.hello);
  });
});
