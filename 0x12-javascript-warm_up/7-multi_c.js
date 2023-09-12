#!/usr/bin/node
/*
this program  that prints x times “C is fun”
*/
const cpt = process.argv[2];
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
for(let i=0 ; i<cpt ; i++){
	console.log('C is fun');
}
