#!/usr/bin/node
// Create a sentence
const format = ' is ';
if (!process.argv[2]) {
  console.log(`undefined ${format} undefined`);
} else if (process.argv.length === 4) {
  console.log(`${process.argv[2]} ${format} ${process.argv[3]}`);
} else if (process.argv.length === 3) {
  console.log(`${process.argv[2]} ${format} undefined`);
}
