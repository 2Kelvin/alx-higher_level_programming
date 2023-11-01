$(function () {
  const divXter = $('#character');
  const ulMovies = $('#list_movies');

  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, function (i, film) {
      ulMovies.append($('<li></li>').text(film.title));
    });
    divXter.text(xterName);
  });
});
