#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(value => value * list.indexOf(value));
console.log(list);
console.log(newList);
