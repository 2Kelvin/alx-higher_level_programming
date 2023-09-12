#!/usr/bin/node
const dict = require('./101-data').dict;
const dt = {};
for (const k in dict) {
  if (dt[dict[k]] === undefined) dt[dict[k]] = [];
  dt[dict[k]].push(k);
}
console.log(dt);
