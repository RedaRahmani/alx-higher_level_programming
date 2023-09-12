#!/usr/bin/node
/*
this program  that prints My number: <first argument converted in integer>
*/
const arg1 = process.argv[2];
const argInt = parseInt(arg1);
if (!argInt) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argInt);
}
