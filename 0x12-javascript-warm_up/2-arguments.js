#!/usr/bin/node
/*
this program display a message depending of the number of args
*/
const cpt = process.argv.length;
if (cpt === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
