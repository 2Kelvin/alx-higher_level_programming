#!/usr/bin/node
// Add
function add (a, b) {
  console.log(a + b);
}
const args = process.argv;
const arg1 = parseInt(args[2]);
const arg2 = parseInt(args[3]);
add(arg1, arg2);
