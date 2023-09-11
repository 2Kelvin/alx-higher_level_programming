#!/usr/bin/node
// Factorial
function factorial (num) {
  if (num === 0 || isNaN(num) || num === 1) return 1;
  else return num * factorial(num - 1);
}
console.log(factorial(parseInt(process.argv[2])));
