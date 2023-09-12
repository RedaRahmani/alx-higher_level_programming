#!/usr/bin/node
/*
this program searches the second biggest integer in the list of arguments.
*/
if (process.argv.length < 4) {
  console.log(0);
} else {
  const liste = process.argv.slice(2).sort(function (a, b) { return b - a; });
  console.log(liste[1]);
}
