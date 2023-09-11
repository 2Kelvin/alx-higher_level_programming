#!/usr/bin/node
// Square
const args = process.argv;
if (parseInt(args[2], 10)) {
  for (let h = 0; h < parseInt(args[2]); h++) {
    console.log('X'.repeat(parseInt(args[2])));
  }
} else console.log('Missing size');
