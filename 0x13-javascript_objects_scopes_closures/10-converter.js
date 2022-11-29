#!/usr/bin/node
/*
Prototype: exports.converter = function (base)
You are not allowed to import any file
You are not allowed to declare any new variable (var, let, etc..)
*/
exports.converter = function (base) {
  // using closure
  return function (num) {
    return num.toString(base);
  };
};
