#!/usr/bin/node
//argument converted to an integer
const num = Number.parseInt(process.argv[2]);

console.log(Number.isNaN(num) ? 'Not a number' : 'My number: ' + num);
