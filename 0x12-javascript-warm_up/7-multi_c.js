#!/usr/bin/node
// I love C
const args = process.argv;
if (parseInt(args[2], 10)) {
  let i;
  for (i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurences');
