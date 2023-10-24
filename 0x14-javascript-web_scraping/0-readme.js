#!/usr/bin/node

const request = require('request');

const alxUrl = process.argv[2];
request(alxUrl, (err, urlResponse, body) => {
    console.err(`error: ${err}`)
    console.log(`code: ${urlResponse.statusCode}`);
});
