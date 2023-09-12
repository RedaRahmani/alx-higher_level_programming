#!/usr/bin/node
/*
this program  that prints x times “C is fun”
*/
const cpt = parseInt(process.argv[2]);
if (!cpt) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < cpt; i++) {
  console.log('C is fun');
}
