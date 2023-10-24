#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request(apiURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);

  const todosList = JSON.parse(body);

  const output = {};
  for (let idUser = 1; idUser < 11; idUser++) {
    let countCompleted = 0;
    for (const todo of todosList) {
      if (idUser === todo.userId) {
        if (todo.completed === true) countCompleted++;
      }
    }
    output[idUser] = countCompleted;
  }
  console.log(JSON.stringify(output));
});
