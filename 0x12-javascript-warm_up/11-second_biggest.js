#!/usr/bin/node
// Second biggest
const args = process.argv;
if (args.length <= 3) console.log(0);
else {
    const arr = args.slice(2).sort(
        (x, y) => x - y
    ).reverse();
    let sec = arr[1];
    console.log(sec);
}
