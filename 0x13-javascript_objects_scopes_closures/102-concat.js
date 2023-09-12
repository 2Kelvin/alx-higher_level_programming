#!/usr/bin/node
const fileSys = require('fs');

let fileData = '';
const file1 = process.argv[2];
const file2 = process.argv[3];
const destFile = process.argv[4];

fileData = fileData.concat(fileSys.readFileSync(file1));
fileData = fileData.concat(fileSys.readFileSync(file2));
fileSys.writeFileSync(destFile, fileData);
