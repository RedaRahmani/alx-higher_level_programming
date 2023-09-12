#!/usr/bin/node
/*
prints the addition of 2 integers
*/
const N1 = parseInt(process.argv[2]);
const N2 = parseInt(process.argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(N1, N2));
