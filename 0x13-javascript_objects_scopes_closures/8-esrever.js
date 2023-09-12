#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  for (let i = list.length - 1; i >= 0; i--) {
    list1.push(list[i]);
  }
  return list1;
};
