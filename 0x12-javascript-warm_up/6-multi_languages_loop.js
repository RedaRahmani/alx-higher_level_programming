#!/usr/bin/node
/*
this program  that prints My number: <first argument converted in integer>
*/
const multiLanguages = {
  first: 'C is fun',
  second: 'Python is cool',
  third: 'JavaScript is amazing'
};

for (const key in multiLanguages) {
  console.log(multiLanguages[key]);
}
