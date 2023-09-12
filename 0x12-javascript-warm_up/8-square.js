#!/usr/bin/node
/*
 this program prints a square
*/
const number = parseInt(process.argv[2]);
if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
