#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];
const wAntillesId = 18;
let filmCount = 0;
request(apiURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);
  const allStarWarsMovies = JSON.parse(body).results;

  for (const movie of allStarWarsMovies) {
    for (const xter of movie.characters) {
      const searchStr = `https://swapi-api.alx-tools.com/api/people/${wAntillesId}/`;
      if (xter === searchStr) filmCount++;
    }
  }
  console.log(filmCount);
});
