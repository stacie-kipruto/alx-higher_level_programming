#!/usr/bin/node
let nArgs = 0;
exports.logMe = function (item) {
  console.log(nArgs + ': ' + item);
  nArgs++;
};
