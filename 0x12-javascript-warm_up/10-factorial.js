#!/usr/bin/node
/*
this program that computes and prints a factorial
*/
const cpt = parseInt(process.argv[2]);
function factorial (cpt) {
  if (!cpt) {
    return (1);
  } else {
    return (cpt * factorial(cpt - 1));
  }
}
console.log(factorial(cpt));
