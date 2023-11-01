$(function () {
  const divXter = $('#character');
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function(data) {
    const xterName = data.name;
    divXter.text(xterName);
  });
});

